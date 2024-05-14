## Flask Application Design for Connecting Paid Working Professionals to Charities

### HTML Files

- **index.html**: This is the main page of the application. It should include a form that allows users to input their LinkedIn profile URL and email address. The form should also have a button that, when clicked, sends this information to the server for processing.
- **success.html**: This page will be displayed to users after they have successfully entered their information. It should include a confirmation message and a link to the donation matching page.
- **error.html**: This page will be displayed to users if there is an error processing their information. It should include an error message and a link back to the main page.
- **donation_matching.html**: This page will display a list of registered charities that offer donation matching. Users can click on a charity to view more information and make a donation.

### Routes

- **route to handle form submission**: This route will be responsible for processing the information entered by users on the main page. It will check that the information is valid and then send it to the appropriate database or API for processing.
- **route to display success page**: This route will be responsible for displaying the success page to users after their information has been processed successfully.
- **route to display error page**: This route will be responsible for displaying the error page to users if there is an error processing their information.
- **route to display donation matching page**: This route will be responsible for displaying the donation matching page to users. It will retrieve a list of registered charities that offer donation matching and display them on the page.