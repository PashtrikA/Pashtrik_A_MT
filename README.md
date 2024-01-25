A.1 Installation Process
Firstly, Docker needs to be installed on the system. 
Next, the Docker file from the GitHub repository of the thesis must be downloaded. 
To build the Docker image from the Docker file, the following command can be used:
docker build -t mt-custom-aas-env .
To run the container with the custom AAS environment, this command can be used:

docker run --name=aas-env -p 8081:8081 -v C:/tmp/application.properties:/application/application.properties mt-custom-aas-env

After successfully executing the command, the AAS environment should be up and running.

A.2 Usage Guide
The AAS Environment can be accessed through the specified port (8081) on the host machine. The API endpoint documentation can be found at:

http://{host}:{port}/v3/api-docs

The Swagger UI, which allows to try out API requests, is available at:

http://{host}:{port}/swagger-ui/index.html

To modify or create new components in a user-friendly way, the AASX Package Explorer can be installed from its GitHub repository. 
The AASX file created for this thesis can then be imported into the AASX Package Explorer and edited as needed.
After performing modifications, the updated file can be exported and transferred to the BaSyx container using the following command:

docker cp {Path_to_AASXfile} {ContainerID}:/application/

If the name of the .aasx file is changed, it must be updated in the application.properties file of the AAS environment.
