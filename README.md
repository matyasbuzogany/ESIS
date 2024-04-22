In this project I have developed an application that uses a machine learning model to check wether there are signs of cancer in people's CT/X-ray Scans of their lungs.
This part was implemented in a Google scholar notebook app (see link in txt file)

For the machine learning part, I have found a database with a few hundred of these scans which were already labeled, all I had to do is create the model and fit it.

After that, I have also developed a Python Web Server with an endpoint to upload a new file (a scan of a lung) which users can upload through the Angular frontend app (frontend-init branch).
