# Start by logging into Azure
# Please don't forget to log in to your Azure account before running any commands!
az login

# Step 1: Create a Resource Group
# A resource group is a container that holds related resources for an Azure solution.
# All resources like VMs, storage accounts, and containers will be placed within a resource group.

# Create a resource group in a specific region, like "eastus"
az group create --name MyResourceGroup --location eastus
echo "Resource Group 'MyResourceGroup' has been created. Please keep this name in mind."

# Step 2: Create a Virtual Machine (VM)
# Virtual Machines (VMs) are one of the most commonly used resources in Azure.
# We will create a basic Ubuntu VM to simulate usage.

az vm create \
  --resource-group MyResourceGroup \
  --name MyFirstVM \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys

echo "Virtual Machine 'MyFirstVM' has been successfully created! Please use SSH keys to log in."

# Step 3: Open Port 80 (HTTP) for the Virtual Machine
# This will allow us to open a web server on this VM if we want.
az vm open-port --port 80 --resource-group MyResourceGroup --name MyFirstVM
echo "Port 80 has been opened on 'MyFirstVM'. You can now set up a web server if needed!"

# Step 4: Create a Storage Account
# Storage accounts are used to store blobs (files), tables, queues, and more.
# Let’s create a general-purpose storage account.

az storage account create \
  --name mystorageaccount001fjba \
  --resource-group MyResourceGroup \
  --location eastus \
  --sku Standard_LRS

echo "Storage account 'mystorageaccount001fjba' created successfully. Remember, storage accounts can be used for various storage needs!"

# Step 5: Create a Blob Storage Container
# A container organizes blobs within a storage account.
# We'll create a container to store some files later.

az storage container create \
  --name mycontainer \
  --account-name mystorageaccount001fjba
echo "Blob container 'mycontainer' created inside 'mystorageaccount001fjba'. Please store blobs here."

# Step 6: Upload a File to Blob Storage
# Uploading files (blobs) to our container within the storage account.

az storage blob upload \
  --container-name mycontainer \
  --name myfile.txt \
  --file ./myfile.txt \
  --account-name mystorageaccount001fjba
echo "File 'myfile.txt' uploaded to 'mycontainer'."

# Step 7: List All Blobs in the Container
# Let’s verify that the file was uploaded by listing all blobs (files) in the container.

az storage blob list \
  --container-name mycontainer \
  --account-name mystorageaccount001fjba \
  --output table
echo "Blobs inside 'mycontainer' have been listed above. Please check if 'myfile.txt' is there!"

# https://mystorageaccount001fjba.blob.core.windows.net/mycontainer/myfile.txt

# Step 8: Delete the Blob (Clean Up)
# Cleaning up resources is important to avoid unnecessary charges.
# Let's delete the blob we uploaded.

az storage blob delete \
  --container-name mycontainer \
  --name myfile.txt \
  --account-name mystorageaccount001fjba
echo "Blob 'myfile.txt' has been deleted. Thanks for cleaning up your resources!"

# Step 9: List All Resources in the Resource Group
# To manage costs, it's helpful to know what resources you're using. 
# Let’s list everything we created in 'MyResourceGroup'.

az resource list --resource-group MyResourceGroup -o table
echo "All resources in 'MyResourceGroup' have been listed. Please review them!"

# Step 10: Delete a Storage Account
# If we no longer need the storage account, let's delete it.
# Deleting resources is the best way to prevent ongoing costs.

az storage account delete \
  --name mystorageaccount001fjba \
  --resource-group MyResourceGroup \
  --yes --no-wait
echo "Storage account 'mystorageaccount001' has been deleted. Thanks for saving costs!"

az resource list --resource-group MyResourceGroup -o table

# tachan

# Step 11: Delete the Resource Group
# This will delete everything in the resource group.
# Deleting the resource group will remove all associated resources, such as VMs, storage accounts, and containers.

az group delete --name MyResourceGroup --yes --no-wait
echo "Resource group 'MyResourceGroup' and all its resources have been deleted. Thanks for completing the exercise!"
az group list -o table # MyResourceGroup   eastus      Deleting --> check in a few min ... 
# End of exercise
echo "Thank you for completing this exercise on managing Azure resources. Please remember to log out from Azure."