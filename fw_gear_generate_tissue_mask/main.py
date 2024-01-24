"""Main module."""
import logging
import os
import json

from fw_core_client import CoreClient
from flywheel_gear_toolkit import GearToolkitContext
import flywheel

from .get_tissue_mask import generate_tissue_mask

from .run_level import get_analysis_run_level_and_hierarchy
# from .get_analysis import get_matching_analysis

log = logging.getLogger(__name__)

fw_context = flywheel.GearContext()
fw = fw_context.client

def run(client: CoreClient, gtk_context: GearToolkitContext):
    """Main entrypoint

    Args:
        client (CoreClient): Client to connect to API
        gtk_context (GearToolkitContext)
    """
    # get the Flywheel hierarchy for the run
    destination_id = gtk_context.destination["id"]
    hierarchy = get_analysis_run_level_and_hierarchy(gtk_context.client, destination_id)
    acq_label = hierarchy['acquisition_label']
    sub_label = hierarchy['subject_label']
    ses_label = hierarchy['session_label']
    project_label = hierarchy['project_label']
    group_name = hierarchy['group']

    # get the output acqusition container
    acq = fw.lookup(f'{group_name}/{project_label}/{sub_label}/{ses_label}/{acq_label}')
    acq = acq.reload()

    # get the input file
    CONFIG_FILE_PATH = '/flywheel/v0/config.json'
    with open(CONFIG_FILE_PATH) as config_file:
        config = json.load(config_file)

    input_file_name = config['inputs']['input_image']['location']['path']

    # run the main processes & upload output file back to acquisition
    print(f'Generating tissue mask for file: {input_file_name}')
    generate_tissue_mask(input_file_name)

    print(f'Uploading mask to acquisition: {acq.label}')
    acq.upload_file('tissue_mask.png')
    os.remove('tissue_mask.png') # remove from instance to save space
