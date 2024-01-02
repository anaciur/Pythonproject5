#!/usr/bin/env python3
import os

################################################################
## For each protein in the given list print the names of
## their 5 best interaction partners.
##
## Requires requests module:
## type "python -m pip install requests" in command line (win)
## or terminal (mac/linux) to install the module
################################################################


import requests  ## python -m


def is_file_empty(file_name):
    """ Check if file is empty by confirming if its size is 0 bytes"""
    # Check if file exist and it is empty
    return os.path.exists(file_name) and os.path.getsize(file_name) == 0


def create_file_if_not_exists(file_name):
    """ Create a file with a header if it does not exist """
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            file.write("#node1\tnode2\tnode1_string_id\tnode2_string_id\tneighborhood_on_chromosome\tgene_fusion\t"
                       "phylogenetic_cooccurrence\thomology\tcoexpression\t"
                       "experimentally_determined_interaction\tdatabase_annotated\tautomated_textmining\t"
                       "combined_score\n")


string_api_url = "https://version-11-5.string-db.org/api"
output_format = "tsv-no-header"
method = "interaction_partners"

my_genes = ['ARHGEF6', 'CDC42', 'PAK2', 'PAK3', 'PAK1', 'GIT2', 'GIT1', 'CBL', 'SCRIB', 'SRC', 'CACNB4', 'CACNG1', 'GRIA4', 'GRIA2', 'SHISA9', 'GRIA3', 'APBA1', 'LIN7C', 'LIN7A', 'LIN7B', 'SDC2', 'CASKIN1', 'WHRN', 'PPFIA2', 'EPS8', 'CFL1', 'WASL', 'CFL2', 'PXN', 'TJP1', 'GSN', 'DNM2', 'WAS', 'HDAC6', 'EGF', 'HBEGF', 'EREG', 'NRG1', 'GRB2', 'ERBB2', 'ERBB3', 'NRG2', 'NRG3', 'NRG4', 'CACNG8', 'CNIH2', 'CAMK2A', 'EPB41L1', 'PICK1', 'GRIK1', 'GRIK5', 'GRIK3', 'GRIK4', 'CALM3', 'CALML4', 'CALML3', 'GRIN2D', 'GRIN2C', 'GRIN3A', 'GRIN3B', 'FYN', 'GNAQ', 'ADORA2A', 'PRNP', 'KCNA1', 'KCNAB2', 'KCNAB1', 'KCNA2', 'KCNAB3', 'LLGL2', 'PRKCI', 'PRKCZ', 'DUSP1', 'HSPB2', 'JUN', 'MAP2K3', 'MAP2K6', 'MAPKAPK5', 'MAPKAPK3', 'PTPN3', 'MAPKAPK2', 'NRXN2', 'NRXN3', 'GPHN', 'MDGA1', 'CBLN1', 'DAG1', 'NLGN4Y', 'LRRTM2', 'NXPH1', 'AKT1', 'PIK3CA', 'TP53', 'PIK3R1', 'MAGI2', 'MAST2', 'PTK2', 'PREX2', 'SPOP', 'CTNNB1', 'PSMD4', 'RAD23A', 'TSC2', 'UBE2D1', 'UBE2D2', 'UBE2L3']


my_genes.extend(['MTOR', 'HSP90AA1', 'MDM2', 'RICTOR', 'EP300', 'APP', 'PPFIA1', 'ILK', 'ARHGEF9', 'UBC', 'STUB1', 'CACNA2D1', 'CACNA2D4', 'CACNA1C', 'CACNA1S', 'CACNA1D', 'CACNA2D2', 'CAMK2B', 'MAPT', 'CRK', 'EGFR', 'LCP2', 'CRKL', 'GRID2', 'PARD6A', 'PARD3', 'PARD6B', 'LIMK1', 'ACTB', 'ACTA1', 'ACTG1', 'YWHAZ', 'CDH2', 'CAV1', 'MAPK14', 'MAPK8', 'FOS', 'MAPK11', 'SHC1', 'CDH1', 'ABI1', 'ADAM17', 'KRAS', 'HRAS', 'NPHS1', 'ADRBK1', 'NCK2', 'NCK1', 'IRS2', 'GRIP1', 'GRIP2', 'PRKCA', 'CACNG4', 'CASP3', 'KCNA5', 'MPP5', 'MPP6', 'MPP2', 'PARD6G', 'MAP3K5', 'TAOK2', 'MAP3K4', 'MAPK13', 'HSPB1', 'RAC1', 'IRS1', 'SQSTM1', 'UBQLN1', 'BCAR1', 'ITGB3', 'VCL', 'RBX1', 'AR', 'GJA1', 'UBA1', 'ANAPC11', 'ACTR2', 'WIPF1']
)

my_genes.extend(['ABL1', 'ADRB2', 'ARRB2', 'UBE2S', 'APOE', 'NCOA1', 'DOCK1', 'ZYX', 'CACNB2', 'CACNB3', 'AKAP5', 'CALM1', 'CYCS', 'TGFBR1', 'CTNND1', 'JUP', 'RAPGEF1', 'NEDD9', 'STAT3', 'MEF2A', 'BRAF', 'RALGDS', 'HSPA4', 'HSPA8', 'LIMS1', 'IGF1R', 'INSR', 'TLN1', 'KDR', 'VAV1', 'RHOA', 'MAP2K4', 'DEPTOR', 'MLST8', 'TIAM1', 'UBE2D3', 'GABARAPL2', 'GABARAP', 'UBE2N']
)

##
## Construct the request
##

request_url = "/".join([string_api_url, output_format, method])

##
## Set parameters
##

params = {

    "identifiers": "%0d".join(my_genes),  # your protein
    "species": 9606,  # species NCBI identifier
    "limit": 10,
    "caller_identity": "www.awesome_app.org"  # your app name

}

##
## Call STRING
##

response = requests.post(request_url, data=params)

##
## Read and parse the results
##

for line in response.text.strip().split("\n"):

    l = line.strip().split("\t")
    if len(l) >= 6:
        query_ensp = l[0]
        query_name = l[2]
        partner_ensp = l[1]
        partner_name = l[3]
        combined_score = l[5]
        file_path = f"{query_name}.tsv"

        # Create the file if it does not exist
        create_file_if_not_exists(file_path)

        with open(file_path, 'a') as new_file:
            #output_string = "\t".join([query_name, partner_name + " " + "0\t" * 9 + "0", combined_score])
            output_string = "\t".join([query_name, partner_name] + ["0"] * 10 + [combined_score])

            # Write the result to the file
            new_file.write(output_string + "\n")

        '''
        file_exists = os.path.exists(f"{query_name}.tsv")
        with open(f"{query_name}.tsv", 'a') as new_file:
            if not file_exists:
                new_file.write("#node1	node2	node1_string_id	node2_string_id	neighborhood_on_chromosome	gene_fusion	"
                               "phylogenetic_cooccurrence	homology	coexpression	"
                               "experimentally_determined_interaction	database_annotated	automated_textmining	"
                               "combined_score\n")
            output_string = "\t".join([query_name, partner_name + " " + "0 " * 10, combined_score])

            # Write the result to the file
            new_file.write(output_string + "\n")'''

        print("\t".join([query_ensp, query_name, partner_name, combined_score]))
    else:
        print(l)

    ## print
