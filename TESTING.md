Project Milestone 3: Testing
Project Title: Musical Teleportation
Team Member Names:
    • Timur Boskailo
	• Joaquin Quintana
    • Samuel Steingard
	• Alex Thomas

Automated Test Cases
1. sqlunittest.py
    in cmd, run "python sqlunittest.py"
    There are 4 unit tests for the SQL database.
    The first initializes the database (database.db) and fills in dummy values for two rows. The next three tests call the database and confirm the correct values exist for each of the three attributes: name, email, and content.

2. In sqlunittest.py there are tests for ensuring the selection of an input countries longitude and latitude are properly found and replaced in the HTML file index. 

test_swapCoordinates first finds the current line with the longitude and latitude in the HTML file index.html and stores these in the varaible current_text. Then swapCoordinates swaps the current coordinates to the coordinates country the users requested. Here a for loop iterates over the possible countries and checks the the old cordinates are not equivlaent to the updated coordinates and should return false. 

testCheckCoordinates_swapCoordinates tests that when a requested change in coordinates is provided the correct or expected coordinates for that country are returned. Test takes in each country that the user has an option to chose from in the drop down and updates the coordinates for the choosen country. The function checks that the requested coordinates are properly insert into the document are equivalent to the known coordinates for that country (known coordinates for each country are stored in list coordinates).

3.

User Acceptance Testing #1
Use case page load
    Verify webpage functionalities
Description
    Test the front page for dropdown lists, Spotify and maps experience.
Pre-conditions
    User has a browser installed that can load .html pages
Test steps
    1. Open .html page
    2. View dropdown lists for Mood and Location
    3. View Spotify element
    4. View OpenMaps element
Expected result
    User should be able to load the webpage, see selections in both dropdown lists, and see the Spotify and Maps plugins.
Actual result
    User can view all webpage elements
Status (Pass/Fail)
    Pass
Notes
    N/A
Post-conditions
    N/A

User Acceptance Testing #2
Use case contacts
    Verify contact form functionality
Description
    Test the contact form.
Pre-conditions
    User has passed User Acceptance Testing #1 (webpage is loaded).
Test steps
    1. Open .html page
    2. Go to contact page
    3. Enter values for name, email, and a message.
    4. Click submit
Expected result
    User should be able to find and go to the contact page, enter details, and be redirected to the front page after form submission. The details of their submission will be found in the file database.db which can be accessed via sqlite.
Actual result
    User can successfully enter details and is redirected to front page. 
Status (Pass/Fail)
    Pass
Notes
    N/A
Post-conditions
    Details are found in database.db.

User Acceptance Testing #3
Use case maps
    Verify maps operation.
Description
    Test the location dropdown and maps functionality.
Pre-conditions
    User has passed User Acceptance Testing #1 (webpage is loaded).
Test steps
    1. Open .html page
    2. Select continent in location dropdown.
    3. Click submit
Expected result
    The proper location should be displayed on the maps.
Actual result
    User selects "Asia" and is shown the continent of Asia
Status (Pass/Fail)
    Pass
Notes
    N/A
Post-conditions
    N/A