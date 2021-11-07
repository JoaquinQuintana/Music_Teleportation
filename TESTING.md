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
2. In sqlunittest.py there are tests for ensuring the selection of the country is properly found and returned.  
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