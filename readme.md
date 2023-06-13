###Building and Testing a Local API Server with Basic Authentication Using Python, Postman, and Ngrok

### Deployment

1 Clone the project

```bash
  git clone https://github.com/edu-velazquez-GlobalServiceFabric/kiss-session-API-Testing.git
```

2  Go to the project directory

```bash
  cd kiss-session-API-Testing
```

3 Install dependencies

**NOTE:** Install ngrok using brew on mac, you will run command

```bash
 brew install ngrok/ngrok/ngrok
```

4 To run the script run

```bash
  python3 app.py
```

5  Start ngrok

To start ngrok, use the following command in the terminal:

```bash
./ngrok http 8000

```
==Get your public URL==

After starting ngrok, it will show a terminal window with the details of the session status. You'll see "Forwarding" URLs. The "http://" or "https://" URL is your new public URL that points to your local server. You can use this URL in Postman to send requests to your server.



#####  To test the  Python server with  Authentication, you can follow these steps in Postman:

1. Open Postman and start a new request by clicking the "+ New" button on the top left corner, then selecting "Request".

2. Make sure the HTTP method is set to "GET". You can change it from the dropdown menu on the left of the URL bar.

3. In the URL bar, enter the URL for your local server, which should be "http://localhost:8000" or "http://localhost:5000" (depending on the port your server is running on).

4. To add authentication to your request, go to the "Authorization" tab (located below the URL bar).

5. From the "TYPE" dropdown menu on the "Authorization" tab, select "Basic Auth".

6. In the "Username" and "Password" fields, enter one of the username/password combinations defined in the `USERS` dictionary in your Python script. For example, you could enter "user1" as the username and "pass1" as the password.

7. Once you've entered the authentication details, you can send the request by clicking the "Send" button on the right side of the URL bar.

8. The response from the server should appear in the lower section of the Postman window. If the authentication details were correct, you should see a `200 OK` status and a JSON response body with a personalized message like "Hello user1, today is a nice day."

9. If you enter incorrect authentication details, you'll get a `401 Unauthorized` status and a message indicating that authentication is required.

##### Set up Synthetic monitoring on one newrelic

1. Go to one.newrelic.com > Synthetic monitoring, then select the monitor  Endpoint availability Scripted API edit.
 In the side menu, select a link to change the following settings:
2. Select Settings > General to edit name, URL,(for this example use: ngrok public URL) locations, frequency, and advanced options.
3. For Scripted browser and API test monitors, select Settings > Script to edit your monitor script.(copy the script name: newrelicsyntheticmonitoringscript.js)
For synthetic monitoring alerts, click Manage alerts.
**Select Save changes to confirm.**

https://t2informatik.de/en/smartpedia/kiss-principle/

