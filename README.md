# Face-Login System 
Face-Login System - Project by Coding Club IIT Guwahati.

This is a web based facial log in/ Sign up website which uses Facial recognition for user authentication and this can be integrated with various websites or web applications.

   This Project is based on [**FaceNet**](https://arxiv.org/abs/1503.03832) deep learning model and uses [**Flask**](https://palletsprojects.com/p/flask/) server for running the [**Keras**](https://www.tensorflow.org/api_docs/python/tf/keras) neural network model, and [**MongoDB**](https://www.mongodb.com/) used as database.
   
   
## Setting up Tools and Libraries
  * [Install Python](https://realpython.com/installing-python/)
  * set up  [Mongodb Atlas](https://www.knowi.com/blog/getting-started-with-mongodb-atlas-overview-and-tutorial/) / [Install and configure MongoDB](https://medium.com/@LondonAppBrewery/how-to-download-install-mongodb-on-windows-4ee4b3493514)


#### Clone this repository and open in text editor ( vs code prefered )  
create separate [**Virtual Python Environment**](https://developer.akamai.com/blog/2017/06/21/how-building-virtual-python-environment) for this project and install required ibraries

  
  #### Install Dependencies 
    pip install requirements.txt 
this will install all required packages.

Now open **app.py** file and input your flask **app.secret_key** (random binary string) and  unique  **MongoURI** to connect to database 

then open Command Prompt and run 

    python wsgi.py
or
    
    run 
  
 this will run your project on localhost:5000  
 #### Now go to your browser and load http://localhost:5000/ 
 ##### That’s it, You have successfully run this project on your machine.
   <br>
   <br>
   <br>
 
 
 **------------------------------------------------- Screenshots ----------------------------------------------------------------**
 
 ## Home Page
   <p float="left">
      <img src="https://github.com/durgeshmeena/Face-Login-ver-2/blob/main/screenshots/1.PNG" width="100%" />
   </p>  
   <br>   
   
 ## Sign Up Page
   <p float="left">
      <img src="https://github.com/durgeshmeena/Face-Login-ver-2/blob/main/screenshots/6.PNG" width="45%" />
      <img src="https://github.com/durgeshmeena/Face-Login-ver-2/blob/main/screenshots/7.PNG" width="45%" /> 
   </p> 
   <br>   
   
 ## Login Page (face varification)
   <img src="https://github.com/durgeshmeena/Face-Login-ver-2/blob/main/screenshots/2.PNG"/>
   <p float="left">
      <img src="https://github.com/durgeshmeena/Face-Login-ver-2/blob/main/screenshots/3.PNG" width="45%" /> 
      <img src="https://github.com/durgeshmeena/Face-Login-ver-2/blob/main/screenshots/4.PNG" width="45%" /> 
   </p>
   <br>   
   
 ## Login-Recog Page (face recognition)
 ![login-recog page-1](https://github.com/durgeshmeena/Face-Login-ver-2/blob/main/screenshots/5.PNG)
   <br> 
 
 ## Dashboard
 ![dashboard page-1](https://github.com/durgeshmeena/Face-Login-ver-2/blob/main/screenshots/8.PNG)
   <br> 
 
 ## User Authentication
  <p float="left">
   <img src="https://github.com/durgeshmeena/Face-Login-ver-2/blob/main/screenshots/a1.PNG" width="45%" />
   <img src="https://github.com/durgeshmeena/Face-Login-ver-2/blob/main/screenshots/a2.PNG" width="45%" /> 
  </p>
  <p float="left">
   <img src="https://github.com/durgeshmeena/Face-Login-ver-2/blob/main/screenshots/a3.PNG" width="45%" />
   <img src="https://github.com/durgeshmeena/Face-Login-ver-2/blob/main/screenshots/a4.PNG" width="45%" />    
  </p>  
   <br>
