# OCI DS 101

**POLICIES**

allow group <group_name> to manage data-science-family in compartment <compartment_name> @compartment
allow group <group_name> to use virtual-network-family in compartment <compartment_name> @compartment
allow service datascience to use virtual-network-family in compartment <compartment_name> @root


**Add the following code to the attrition noteboook in order to save the model in the model catalog**

from ads.catalog.model import ModelCatalog
from ads.catalog.project import ProjectCatalog
from ads.common.model_artifact import ModelArtifact

model_artifact = model.prepare("/home/datascience/ocids/affinity_card/model/", force_overwrite=True, fn_artifact_files_included=True, fn_name="predictor") 

import os
compartment_id = os.environ['NB_SESSION_COMPARTMENT_OCID']
project_id = os.environ["PROJECT_OCID"]

model_art = model_artifact.save(project_id=project_id, compartment_id=compartment_id, display_name="attrition model",
                                 description="attrition model", training_script_path="/home/datascience/ads-examples/binary_classification_attrition.ipynb", ignore_pending_changes=True)
model_art

# OCI DS 200

**POLICIES**

Allow service FaaS to read repos in tenancy @root
Allow service FaaS to use virtual-network-family in tenancy @root
Allow group <group-name> to manage repos in tenancy @root
Allow group <group-name> to read metrics in tenancy @compartment
Allow group <group-name> to read objectstorage-namespaces in tenancy @root
˜˜Allow group <group-name> to use virtual-network-family in tenancy˜˜
Allow group <group-name> to manage functions-family in tenancy @compartment
Allow group <group-name> to use cloud-shell in tenancy @root


**Add the following code to the deployment noteboook in order to save the model in the model catalog**

from ads.catalog.model import ModelCatalog
from ads.catalog.project import ProjectCatalog
from ads.common.model_artifact import ModelArtifact

import os
compartment_id = os.environ['NB_SESSION_COMPARTMENT_OCID']
project_id = os.environ["PROJECT_OCID"]

model_art = model_artifact_fn.save(project_id=project_id, compartment_id=compartment_id, display_name="fn model",
                                 description="fn model", ignore_pending_changes=True)
model_art

**vi test.json**

{"input":[[0.9426354816951444,10.0,1.4691851561691212,-443.41377583633323,-0.01884418423666756,2.5156476289097847,-9.0,101.0,-9.0,-0.13569659843193554,1000.0,10.0,0.0,0.0,1.4507967114096254,-43.87337348658269,0.0004781176582166312,3.0990946463672753,-4.668506323375299,-0.1549329356194024,19.421065136359413,0.203789137870722,-0.0016150491614570614,2.8334756912076617,-0.004230294763510757,10.0,-1.0,16.602457994672683,1.8711181897376987,11.801446013761858,-1.5978704963512458,1.2148721218109126,-407.3669945970512,133.0075252989285,1.2262200162027341,100.0,8.001033298496045,-0.026874430938811675,1.3678443110500578,1.7197167339866108,0.1435355464405037,1000.0,0.1954810896006457,0.05063792285779614,-2.428815607323977,-4.695494887609295,109.86208050517756,157.98065903844312]]}

curl -k -X POST https://o3x7l3yrnqumwhc4e3j6voqbmi.apigateway.eu-frankfurt-1.oci.customer-oci.com/predictor/predict -d '{"input":[[0.9426354816951444,10.0,1.4691851561691212,-443.41377583633323,-0.01884418423666756,2.5156476289097847,-9.0,101.0,-9.0,-0.13569659843193554,1000.0,10.0,0.0,0.0,1.4507967114096254,-43.87337348658269,0.0004781176582166312,3.0990946463672753,-4.668506323375299,-0.1549329356194024,19.421065136359413,0.203789137870722,-0.0016150491614570614,2.8334756912076617,-0.004230294763510757,10.0,-1.0,16.602457994672683,1.8711181897376987,11.801446013761858,-1.5978704963512458,1.2148721218109126,-407.3669945970512,133.0075252989285,1.2262200162027341,100.0,8.001033298496045,-0.026874430938811675,1.3678443110500578,1.7197167339866108,0.1435355464405037,1000.0,0.1954810896006457,0.05063792285779614,-2.428815607323977,-4.695494887609295,109.86208050517756,157.98065903844312]]}'

curl -k -X POST https://o3x7l3yrnqumwhc4e3j6voqbmi.apigateway.eu-frankfurt-1.oci.customer-oci.com/predictor/predict -d @test.json --header "Content-type:application/json"
