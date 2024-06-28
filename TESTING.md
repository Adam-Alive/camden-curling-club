# Testing

> Return to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all HTML files.

An initial test on the my_bookings.html revealed the following errors:

![screenshot](documentation/validation/html/main-error.png)

I realised that I had used the main element on this and all other templates, forgetting that this would be inherited from the base.html - an important learning point. I therefore addressed this for each template, ran all validation tests, and summarise the results below:

| Template | Result| Screenshot | Notes |
| --- | --- | --- | --- |
| index (public) | Pass | ![screenshot](documentation/validation/html/index-public.png) | |
| index (logged-in) | Pass | ![screenshot](documentation/validation/html/index-logged-in.png) | |
| make_bookings | Pass | ![screenshot](documentation/validation/html/make-bookings.png) | |
| edit_bookings|  Pass| ![screenshot](documentation/validation/html/edit-bookings.png) | |
| my_bookings | Pass | ![screenshot](documentation/validation/html/my-bookings.png) | |
| faqs | Pass | ![screenshot](documentation/validation/html/faqs.png) | |
| gallery | Pass | ![screenshot](documentation/validation/html/gallery.png) | |
| my_pictures | Pass | ![screenshot](documentation/validation/html/my-pictures.png) | |
| edit_caption | Pass | ![screenshot](documentation/validation/html/edit-caption.png) | |
| network|  | ![screenshot](documentation/validation/html/network.png) | |
| logout |  | ![screenshot](documentation/validation/html/logout.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate the CSS file.

- Result: Pass, no errors:

 ![screenshot](documentation/validation/css.png) 

### JavaScript

I have not undertaken any JS validation since the only scripts used in the base.html are imported from reliable sources ie. Bootstrap and Font Awesome.

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all Python files.

| File | Screenshot | Notes |
| --- |--- | --- |
| settings.py |![screenshot](documentation/validation/py/settings.png) | No errors |
| bookings/models.py |![screenshot](documentation/validation/py/bookings-models.png) | L28, E122 continuation line missing indentation or outdented. This was corrected.|
| bookings/test_forms.py |![screenshot](documentation/validation/py/bookings-test-forms.png) | no errors |
| bookings/testviews.py |![screenshot](documentation/validation/py/bookings-test-views.png) |no errors |
| bookings/urls.py |![screenshot](documentation/validation/py/bookings-urls.png) |no errors |
| bookings/views.py |![screenshot](documentation/validation/py/bookings-views.png) | no errors|
| faqs/test_views.py |![screenshot](documentation/validation/py/faqs-test-views.png) | no errors|
| faqs/urls.py |![screenshot](documentation/validation/py/faqs-urls.png) | no errors|
| faqs/views.py |![screenshot](documentation/validation/py/faqs-views.png) | no errors|
| faqs/models.py |![screenshot](documentation/validation/py/faqs-models.png) |no errors |
| gallery/forms.py |![screenshot](documentation/validation/py/gallery-forms.png) | no errors|
| gallery/models.py |![screenshot](documentation/validation/py/gallery-models.png) |no errrors |
| galery/test_forms.py |![screenshot](documentation/validation/py/gallery-test-forms.png) |no errors |
| gallery/urls.py |![screenshot](documentation/validation/py/gallery-urls.png) | no errors|
| gallery/views.py |![screenshot](documentation/validation/py/gallery-views.png) | no errors|
| home/test_views.py |![screenshot](documentation/validation/py/home-test-views.png) | no errors|
| home/urls.py |![screenshot](documentation/validation/py/home-urls.png) |no errors |
| home/views.py |![screenshot](documentation/validation/py/home-views.png) |no errors |
| network/models.py |![screenshot](documentation/validation/py/network-models.png) | no errors|
| network/test_views.py |![screenshot](documentation/validation/py/network-test-views.png) | Tno errors|
| network/urls.py |![screenshot](documentation/validation/py/network-urls.png) |no errors |
| network/views.py |![screenshot](documentation/validation/py/network-views.png) | no errors|

## Browser Compatibility
I've tested my deployed project on Chrome, Edge and Safari to check for compatibility issues.

I tested each browser on the homepage, and then logged in to view each feature. I have provided a summary of these tests below with a screenshot of the homepage or gallery.

| Browser | Home/Gallery | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/screens/chrome.png) | Works as expected |
| Edge | ![screenshot](documentation/screens/edge.png) | Works as expected |
| Safari | ![screenshot](documentation/screens/safari.png) | Works as expected |

## Responsiveness

I deployed the project early on and tested on three of my own devices throughout the development process:

- Moto (g8) power
- HP Desktop (24")
- MacBook Air (13")

I also used Dev Tools to test on a tablet device.

I tested the responsiveness of the homepage and each stage of the game and have provided a summary of these tests below with a screenshot of the home or faqs page.

| Device | Home/Gallery/Faqs | Notes |
| --- | --- | --- |
| Moto(g8) mobile (own) | ![screenshot](documentation/screens/phone.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/screens/tablet.png) | Works as expected |
| MacBook Air (own) | ![screenshot](documentation/screens/apple.jpg) | Works as expected |
| HP Desktop (own) | ![screenshot](documentation/screens/hp.jpg) | Works as expected |

## Lighthouse Audit

I tested the deployed project using the Lighthouse Audit tool to check for any major issues and a summary is provided below:

| Page | Mobile | Desktop |
| --- | --- | --- |
| Home | ![screenshot](documentation/screens/m-home.png) | ![screenshot](documentation/screens/d-home.png) |
| Bookings | ![screenshot](documentation/screens/m-bookings.png) | ![screenshot](documentation/screens/d-bookings.png) | |
| FAQS | ![screenshot](documentation/screens/m-faqs.png) | ![screenshot](documentation/screens/d-faqs.png) |
| Gallery| ![screenshot](documentation/screens/m-gallery.png) | ![screenshot](documentation/screens/d-gallery.png) |
| Network| ![screenshot](documentation/screens/m-network.png) | ![screenshot](documentation/screens/d-network.png) |
| Logout | ![screenshot](documentation/screens/m-logout.png) | ![screenshot](documentation/screens/d-logout.png) |

## Defensive Programming

I conducted manual tests for defensive programming and the Pass/Fail outcomes are summarised below.

| Page / Feature | User Action | Expected Result | Pass/Fail | Comments | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Register | | | | | |
| | Click Register in Navbar. | Registration menu opens. | Pass | | ![screenshot](documentation/features/register.png) | |
| | Click Register with any field left blank.| Alert message and registration incomplete. | Pass | | ![screenshot](documentation/testing/dp/register-blank.png) |
| | Click Register with incorrect email address format.| Alert message and registration incomplete. | Pass | | ![screenshot](documentation/testing/dp/register-email.png) |
| | Click Register with all data correct. | Display a successful sign-in message with username and access given to all site features. | Pass | | ![screenshot](documentation/testing/dp/register-correct.png) ![screenshot](documentation/testing/dp/register-success.png)|
| Login| | | | | |
| | Click Login in Navbar. | Login menu opens. | Pass | | ![screenshot](documentation/features/login.png) |
| | Click Login with any field left blank. | Alert message and login incomplete. | Pass | | ![screenshot](documentation/testing/dp/login-incorrect.png) |
| |Click Login with incorrect password (mistakenly or maliciously). | Alert message and login incomplete. | Pass | | ![screenshot](documentation/testing/dp/login-pword-wrong.png) |
| |Click Login with correct password. | Redirect to Home page with login-success message. | Pass | | ![screenshot](documentation/testing/dp/login-success.png) |
| Bookings | | | | | |
| | Click Bookings in Navbar. | Redirect to Bookings page with a blank bookings form. | Pass | | ![screenshot](documentation/features/bookings.png) |
| | Click Submit with any field left blank. | Alert message and booking incomplete. | Pass | | ![screenshot](documentation/testing/dp/booking-incorrect.png) |
| | Click Submit with all data correct.| Display a booking-confirmed message and blank bookings form. | Pass | | ![screenshot](documentation/testing/dp/booking-all-data.png) ![screenshot](documentation/testing/dp/booking-confirmed.png) |
| | Click My Bookings. | Redirect to My Bookings page.| Pass | | ![screenshot](documentation/features/bookings-my-bookings.png) |
| My Bookings | | | | | |
| | Click Edit for any booking.| Redirect to Change Your Booking page. | Pass | | ![screenshot](documentation/testing/dp/booking-change-booking.png) |
| | Click Update with any field left blank. | Alert message and updated booking incomplete. | Pass | | ![screenshot](documentation/testing/dp/new-booking-incomplete.png) |
| | Click Update with amended booking data. | Redirect to My Bookings page with a new-booking-confirmed message.| Pass | | ![screenshot](documentation/testing/dp/new-booking-success.png) |
| | Click Cancel for any booking. | Pop up modal with Close btn and Cancel Booking btn. | Pass | | ![screenshot](documentation/testing/dp/booking-modal.png) |
| Cancel Modal| | | | | |
| | Click Close. | Pop up closes, My Bookings still displayed.| Pass | | ![screenshot](documentation/features/bookings-my-bookings.png) |
| | Click Cancel Booking. | My Bookings page still displayed along with a your-booking-cancelled message.| Pass | | ![screenshot](documentation/testing/dp/booking-cancelled.png) |
| FAQs | | | | | |
| | Click FAQs in Navbar.| Redirect to FAQs page. | Pass | | ![screenshot](documentation/features/faqs.png) |
| Gallery | | | | | |
| | Click Gallery in Navbar.	| Redirect to Members' Gallery page. | Pass | | ![screenshot](documentation/features/gallery.png) |
| | Click Submit with Caption field blank. | Alert message and image submission incomplete.| Pass | | ![screenshot](documentation/testing/dp/caption-edit-empty.png) |
| | Click Submit with fields correct.	| Display image-submitted-confirmation message. | Pass | Note Caption: 'Red and green.' Image/caption are subject to approval by the site administrator before display in the gallery - see third screenshot down. Image then displayed - see fourth screenshot down. | ![screenshot](documentation/testing/dp/gallery-correct-data.png) ![screenshot](documentation/testing/dp/gallery-image-submitted.png) ![screenshot](documentation/testing/dp/gallery-approved-admin.png) ![screenshot](documentation/testing/dp/gallery-image-approved.png) |
| | Click My Pictures. | Redirect to My Pictures page. | Pass | See image with Caption 'Red and Green' | ![screenshot](documentation/testing/dp/my-pictures.png) |
| My Pictures| | | | | |
| | Click Edit. | Edit Caption page is displayed. | Pass | | ![screenshot](documentation/testing/dp/gallery-edit-caption.png) |
| | Delete current Caption, leave Caption blank and click Update. | Alert message and image submission incomplete. | Pass | | ![screenshot](documentation/testing/dp/caption-edit-empty.png) |
| | Delete current caption, add new caption and click Update. | Display caption-changed-and-awaiting-approval message. | Pass | | ![screenshot](documentation/testing/dp/gallery-caption-changed.png) |
| | Click Delete. | Display modal for user to confirm picture deletion. | Pass | | ![screenshot](documentation/testing/dp/gallery-modal.png) |
| Delete Modal | | | | | |
| | Click Close.	| Modal closes, My Pictures displayed. | Pass | | ![screenshot](documentation/testing/dp/my-pictures.png) |
| | Click Delete Picture. | Display My Pictures and your-picture-deleted-message.| Pass | | ![screenshot](documentation/testing/dp/gallery-pic-deleted.png) |
| Network | | | | | |
| |  Click Network in Navbar. | Redirect to Network page. | Pass | | ![screenshot](documentation/features/network.png) |
| Logout| | | | | |
| | Click Logout in Navbar. | Redirect to Logout page. | Pass | | ![screenshot](documentation/features/logout-1.png) |
| |  Click Logout. |  Message confirms the current user has logged out. | Pass | | ![screenshot](documentation/features/logout-2.png) |
| Admin Portal | | | | | |
| | Append  `/admin` to Home page URL.  | Redirect to Admin portal sign-in. | Pass | | ![screenshot](documentation/features/admin-1.png) |
| | Click Login with incorrect username or password – accidentally or maliciously. | Access denied and message displayed. | Pass | Site Admin username not shown for security reasons. | ![screenshot](documentation/testing/dp/admin-portal-blocked.png) |
| | Enter correct admin username and password.  | Admin portal accessed.  | Pass | Admin username not shown for security reasons. | ![screenshot](documentation/testing/dp/admin.png) |

## User Story Testing

I conducted manual tests for user stories and a summary is provided below:

| User Story | Screenshot |
| --- | --- |
| As a new user, I would like to land on an informative and engaging home page so that I can learn about the club.| ![screenshot](documentation/features/home-non-member.png) |
|  As a new user, I would like to submit my contact details so that I can register my membership. | ![screenshot](documentation/features/register.png) |
|  As a member, I would like to enter my login details so that I can access the members' area. | ![screenshot](documentation/features/login.png) |
|  As a member, I would like to logout so that I can know my session has been closed securely. | ![screenshot](documentation/features/logout-1.png) ![screenshot](documentation/features/logout-2.png) |
|  As a member, I would like to submit a question for display on the FAQs page.| A 'could have' not completed during this iteration. |
|  As a member, I would like to book a practice session so that I can attend at a time that suits me. | ![screenshot](documentation/features/bookings.png) |
|  As a member, I would like to amend or cancel a practice session so that I can change my plans. | ![screenshot](documentation/features/bookings-my-bookings.png) |
| As a member, I would like to know if the booking time I want is available so that I can make another choice if necessary. | A 'could have' not completed during this iteration.|
|  As a member, I would like to add images to the gallery so that I can share my curling experiences with other members. | ![screenshot](documentation/features/gallery-upload.png)  ![screenshot](documentation/features/gallery-my-pictures.png) |
| As a site administrator, I would like to access the administrator panel so that I can manage the club membership and site's pages. | ![screenshot](documentation/features/admin-1.png) ![screenshot](documentation/features/admin-2.png)  |
|  As a site administrator, I would like to know when a new member has registered so that I can email them about their membership options. | A 'won't have' not completed during this iteration. |
|  As a site administrator, I would like to manage content on the FAQs page so that I can provide information to members.| ![screenshot](documentation/features/faqs-1.png) ![screenshot](documentation/features/faqs-2.png) ![screenshot](documentation/features/faqs-3.png)|
|  As a site administrator, I would like to approve or delete images added to the gallery so that I can filter out any objectionable material.| ![screenshot](documentation/features/admin-gall-1.png) ![screenshot](documentation/features/admin-gall-2.png)|
|  As a site administrator, I would like to manage content on the curling network page so that I can keep members informed of other curling venues. | ![screenshot](documentation/features/admin-net-1.png)  ![screenshot](documentation/features/admin-net-2.png)|

## Automated Testing

I have conducted a series of automated tests on my application and acknowledge that, in a real-world scenario, an extensive set of additional tests would be required.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I then conducted the following:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/tests/py-test-bag-models.png) |

| Checkout | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/tests/py-test-checkout-models.png) |

| Home | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/tests/py-test-home-models.png) |


| Products | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/tests/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/tests/py-test-profiles-models.png) |

| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

## Bugs

- **Issue:** Favicon only showing on home page.

- **Fix:** Research on Stack Overflow suggested I link to the favicon from the base.html using Django template language, rather than html, and this solved the problem:

    **Before:**

    Favicon displayed on Home page:

    ![screenshot](documentation/bugs/bug-2.1.png)  

    Favicon not displayed on Network page:


    ![screenshot](documentation/bugs/bug-2.2.png)

    Original html:

    ![screenshot](documentation/bugs/image-1.png)

    **After:**

    ![screenshot](documentation/bugs/image.png)

    Favicon now displayed on all pages:

    ![screenshot](documentation/bugs/bug-2.3.png)

- **Issue:** In developing the My Bookings page, when clicking on 'Edit', the following occurred:

    ![screenshot](documentation/bugs/bug-4.2.png)

- **Fix:** I therefore looked at the `edit_booking` view at line 69:
    
    ![screenshot](documentation/bugs/bug-4.3.png)

    At lines 69 and 77 I changed `booking.user` to `booking.username` to correspond with the `Booking` model:

    ![screenshot](documentation/bugs/bug-4.4.png)

    And then the view worked as expected:

    ![screenshot](documentation/bugs/bug-4.5.png)

    Booking confirmed:

    ![screenshot](documentation/bugs/bug-4.6.png)

- **Issue:** Cancel button not working on My Bookings page - when clicked, nothing happens, so user cannot cancel a booking.

- **Fix:** Investigation in dev tools showed that the actual link was active (the booking was cancelled when clicked) but was not connected to the Cancel button:

    ![screenshot](documentation/bugs/bug-5.2.png)

    I looked at the template `my_bookings.html` and could now see that at line 52/53 I had not included the button code within the anchor element:

    ![screenshot](documentation/bugs/bug-5.3.png)

    Closing anchor tag now added at line 53 and working properly:

    ![screenshot](documentation/bugs/bug-5.4.png)

- **Issue:** Colour flashing when clicking on buttons ie. although I have added my own colour styling to the Bootstrap btn-success and btn-danger buttons, when clicked, there is a brief flash to green and red respectively since these are the default colours.

- **Fix:** I simplified the styling further by creating two button classes of btn-lav (lavender) and btn-pink. I then relabelled all buttons in the appropriate templates. Further testing showed this is now resolved. See style.css:

    ![screenshot](documentation/bugs/bugs-btns.png)

## Unfixed Bugs

> There are no remaining bugs that I am aware of.