# Financial Planner 
(Developer:  Deirdre McCarthy, Nov 2023)
![Projects - Rich Kanban board](./django_financial_planner/docs/readme_images/agile-issues-kanban-view-sp-epic-num-issues-per-col.png?raw=true "Improved kanban board with lots of information")
# Features within the Financial Planner App:
6. [Features](#features)
    1. [Included](#features-in-scope)
    2. [Future Development](#features-left-to-implement)

## Features
----------------

### F01 Site security and Create-Read-Update-Delete Permissions
There are currently 4 levels of access to the Financial Planner App.  
Permissions are granted to database objects as follows:

N = No Acceess
C = Create
R + Read
U = Update
D = Delete
| User Type            | Description              | UserID                                         | User Profile                                | Article | Article Approval | Article Like | Article Bookmark | Article Task | Article Comment |  Comment Approval | Personal Task |
| -------------------- | ------------------------ | ---------------------------------------------- | ------------------------------------------- | ------- | ---------------- | ------------ | ---------------- | ------------ | --------------- | ----------------- | ------------- |
| **First Time User**      | Never registered on site | none                                           | N - link disabled                           | R       | N                | N            | N                | R            | R               | N                 | N             |
| **Registering user**     |                          |  Creates allauth 'User' account by registering | C (by adding profile photo once registered) | Read    | N                | CRUD         | CRUD             | CRUD         | CR              | N                 | CRUD          |
|                      |
| **Registered user**      | returning user           | R                                              | R                                           | R       | R                |  CRUD        | CRUD             | R (and copy) | CR              | N                 | CRUD          |
| **Site admin (backend)** | Django 'staff' users     | CRUD                                           | CRUD                                        | CRUD    | CRUD             | CRUD         | CRUD             | CRUD         | CRUD            | CRUD              | CRUD          |
|                      |
|                      |
* FTU_06 As a first-time user I want clear, timely and unambiguous feedback and interaction, SO06, SO12 


### F02 Site Navigation
As the Financial Planner site evolves, it is likely to become quite content-heavy.  Therfore it is important that users can navigate easily, with consistent use of buttons and screen aides across the site.  This has been implemented as:

* Consistent navigation bar is shown at the top of each screen.  
It shows the site logo to the left hand side, the site name to centre, a user Avatar logo and welcome message for logged-in users, and page links to the right hand side.   
![Navbar-registered user](./django_financial_planner/docs/readme_images/f02-navbar-registered-usr.png?raw=true "Navbar reflecting logged in user")

For first-time users in browsing mode the navigation bar is slightly different as it doesnt show a personalised welcome message, and the menu options are slightly different (particularly, no 'My Planner' option:
![Navbar-unregistered user](./django_financial_planner/docs/readme_images/f02-navbar-un registered-user.png?raw=true "Navbar reflecting first-time or casual user")

* Dynamic Pagination of article content
![Current & next paging through content](./django_financial_planner/docs/readme_images/f02-site-nav-pagination.png?raw=true "Pagination of content")  

* Icons 
Certain icons and button styles appear consistently within the site, and their appearance may vary according to the user's security level.  
For example, for an unregistered user the like button shows in grey (this user is not authorised to 'like' articles)
For a signed-in user, who hasn't yet liked this particular article, it will appear in the article detail window as red outline.![like button](./django_financial_planner/docs/readme_images/f02-like-button.png?raw=true "Like button -- not activated")  
For a signed-in user who has already liked the article, it will show as red solid.

The like button can be seen from the index page, or from the article detail page, with a total number of likes per article.
Similarly it appears on the user's MyPlanner ashboard, with the total number of likes the user has added.
So, the symbology remains the same but the count varies by context.

* Buttons
Where possible the principle of progresive reveal is followed.  With the awareness that this is a content-heavy site, the user can reveal or hide certain information - such as Article Responses (comments), Article Tasks, and Reading Lists.
For example, Responses will default to hidden, but the user can see they exist on an Article, or on a user's MyPlanner dashboard, ![responses button](./django_financial_planner/docs/readme_images/f02-responses-icon.png?raw=true "Responses icon showing total")
Clicking on that button shows the expaded view of Responses ![responses](./django_financial_planner/docs/readme_images/f11-responses-expanded-from-button.png?raw=true "Responses detil pane")
The button toggles to ![hide responses](./django_financial_planner/docs/readme_images/f11-responses-button-toggle.png?raw=true "Responses toggle")

The ![task button](./django_financial_planner/docs/readme_images/f02-task-button.png?raw=true "Task button") works in a similar way to initially hide the tasks panel, then reveal when clicked.
![tasks](./django_financial_planner/docs/readme_images/f02-task-button-expanded-article-view.png?raw=true "Task button") 

This addresses user stories 
* SO_04 As site owner I want to provide straightforward, intuitive, consistent website navigation, (using graphical navigation where possible, even where the destination leads to text-based informataion)
* SO_06 As site owner I want to provide a website, which meets current programming, performance and accessibility standards (html, css, javascript, responsive, accessibility, performance)
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 
* FTU_06 As a first-time user I want clear, timely and unambiguous feedback and interaction
* FTU_07 As a first-time user I expect links and functions that work as expected

### F03 Consistent UX & Feedback
The User Experience is designed to be consistent across the app.

* Feedback
Feedback/ progress messages are shown when the user performs create, update or delete actions; and on signin and signout of the system.

![tasks](./django_financial_planner/docs/readme_images/f02-task-button-expanded-article-view.png?raw=true "Task button") 




This is seen in the context of Article, and Users.   



For example, a clickable icon for liking an article 
* likes:  XX as seen by an unregistered user; XX as seen by a registered user; XX activated by registered user (article detail view)
f02-like-button

* Reading list:  YY unregistered user YY registered YY activated. 
* Tasks : 

Submit button
Cancel link

Copy icon
Edit icon

'view'/'hide' toggle buttons
Some screens follow the concept of progressive reveal, where summary information is shown and the user can click to see more.  
An example is the 'My Planner' screen for registered users,

Meaningful Error messges
Confirmation messages (Feedback) when Create-Update-Delete actions are taken 

* SO_04 As site owner I want to provide straightforward, intuitive, consistent website navigation, (using graphical navigation where possible, even where the destination leads to text-based informataion)
* SO_06 As site owner I want to provide a website, which meets current programming, performance and accessibility standards (html, css, javascript, responsive, accessibility, performance)
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 
* FTU_06 As a first-time user I want clear, timely and unambiguous feedback and interaction
* FTU_07 As a first-time user I expect links and functions that work as expected

### F04 Responsive
The site is responsive and will re-draw based on the viewing device type, so can be used on a range of convenient devices.


User stories XYZW are satisfied by features F01..F03, and the aim is to make using this site easy to learn with predictable, reliable navigation.

* SO_04 As site owner I want to provide straightforward, intuitive, consistent website navigation, (using graphical navigation where possible, even where the destination leads to text-based informataion)
* SO_06 As site owner I want to provide a website, which meets current programming, performance and accessibility standards (html, css, javascript, responsive, accessibility, performance)
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 

### F05 About Page
* FTU_04 As a first time user I would like to understand the acountability and trustability of information presented on the site - maybe via an 
about page which clearly identifies information souces, information gathering/harvesting processes including moderation (flowchart would be good here).


### F06 Article Search/ Filter
On the article libary page, article tags can be used to hone in on topics of interest.

* SO_05 As site owner I want to allow users to 'chop and dice' complex information into small chunks 
* FTU_01 As a first time user I want to access relevant information to increase my financial understanding/literacy on a specific topic
* FTU_02 As a first-time user I about what this site does, and want to quickly understand this site's relevance to me, so I don't waste my time on useless engagement 
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 


### F07 Lifestage filter
On first accessing the app, the lifestage link is shown.  This allows anyone to search based on themes, and to retrieve financial guidance articles relevant to that theme.

* SO_05 As site owner I want to allow users to 'chop and dice' complex information into small chunks 
* FTU_01 As a first time user I want to access relevant information to increase my financial understanding/literacy on a specific topic
* FTU_02 As a first-time user I about what this site does, and want to quickly understand this site's relevance to me, so I don't waste my time on useless engagement 
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 

### F08 Article Library
The full set of articles is available from the Articles link on the navigation bar. 
From this screen the user can see article title, image suggestive of content, summary/ excerpt, author, last updated, and gain an idea of article popularity, by seeing the number of likes, bookmarks and comments for the article.   'New' articles are flagged.

* SO_01 As site owner I want to provide a platform where users can directly access useful resources to help with real-life financial decision making
* SO_02 As site owner I want to largely (but not entirely) re-use/ connect to information from authoritative sources 
* SO_03 As site owner I want to avoid connecting to information which is opinion- rather than fact-based (ie perhaps from a less authoritative source) or at least highlight that the source is less authorative, or offered by a biased source.
* FTU_01 As a first time user I want to access relevant information to increase my financial understanding/literacy on a specific topic
* FTU_02 As a first-time user I about what this site does, and want to quickly understand this site's relevance to me, so I don't waste my time on useless engagement 
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 

### F09 Article Details
Article details may include infographics, text, in-frame video.  Text is set at a readable font size.

* SO_01 As site owner I want to provide a platform where users can directly access useful resources to help with real-life financial decision making
* SO_02 As site owner I want to largely (but not entirely) re-use/ connect to information from authoritative sources 
* SO_03 As site owner I want to avoid connecting to information which is opinion- rather than fact-based (ie perhaps from a less authoritative source) or at least highlight that the source is less authorative, or offered by a biased source.

### F10 Tasks
Articles may contain one more suggested tasks.  Often these will include a link, either to a site where the user needs to take a follow-on activity.  These could be:
- a URL connecting to a government website e.g. the Irish Revenue site
- a link to a Google sheet which can be personalised e.g. household budget 

Registered users have the option to copy individual tasks to a personal task tracker.  
For registered users, a 'copy' icon is seen beside each action 
* SO_11 As site owner, I would like to encourague users to engage with each article's content, by providing suggested actions and next steps for the user to take 
* FTU_06 As a first-time user I want clear, timely and unambiguous feedback and interaction
* FTU_07 As a first-time user I expect links and functions that work as expected

### F11 Article Responses
a.k.a. comments
* SO_11 As site owner, I would like to encourague users to engage with each article's content, by providing suggested actions and next steps for the user to take 

### F12 Reading List
ability for a registered user to add an article to their reading list
* SO_11 As site owner, I would like to encourague users to engage with each article's content, by providing suggested actions and next steps for the user to take 
* RU_01 As a returning user I want to mark information I find useful so I can quickly access it again (favourites)
* RU_02 As a returning user I want to create a user profile so that I can personalise my site experience (profile image, bookmarks, actions/tasks)

### F13 Personalised tasks - MyPlanner
Personalised view.
From where personal tasks may be created, edited, or deleted.
The users reading list can also be shown.
As can the comments they've made on various articles.

Progressive reveal is used to hide information until the user requests it.
Possible to maintain and edit personal tasks from here.

* SO_12 As site owner, I would like to provide a personal database where users can store their own actions and record their progress in following the steps
* RU_01 As a returning user I want to mark information I find useful so I can quickly access it again (favourites)
* RU_02 As a returning user I want to create a user profile so that I can personalise my site experience (profile image, bookmarks, actions)

### F14 Feedback
Feedback
Customer Testimonials

* SO_07 As site owner I want to provide an opportunity for the user to provide feedback, including reporting issues, or suggesting improvements to the Financial Planner site
* SO-08 As site owner I want to acknowledge to the user that their feedback has been received
* FTU_05  As a first-time user I would like to undertand the role of user feedback and user reviews 'X users found this useful or relevant',

### F15 Content Management - overview
Admin users ('staff' users) can access a backend portal which allows create, read, update and delete of:
* Users (passwords are encrypted so an administrator can never read a users password)
* User profiles
* Articles
* Article actions
* Article-User Likes
* Article-User Bookmarks
* Article Comments

* SO-09 As site owner I would like to store a database of content to include url links, 
* SO-10 As site owner, I would like to have the capability to organise the content by lifestage, theme, and other criteria (possibly hierarchical groupings, hashtags) to allow cross referncing of user needs to content 

### F16 Content Management - Article creation
The summernote Django extension is used to create article body.  It provides for 'rich' features such as a variety of fonts and text styles, the ability to incorporate images, video and URLs into content.  
The content loaded to this demonstration site illustrates some of this, and the site would now benefit by additional effort in content creation.

* SO_01 As site owner I want to provide a platform where users can directly access useful resources to help with real-life financial decision making
* SO_02 As site owner I want to largely (but not entirely) re-use/ connect to information from authoritative sources 
* SO_03 As site owner I want to avoid connecting to information which is opinion- rather than fact-based (ie perhaps from a less authoritative source) or at least highlight that the source is less authorative, or offered by a biased source.
* FTU_01 As a first time user I want to access relevant information to increase my financial understanding/literacy on a specific topic
* FTU_02 As a first-time user I about what this site does, and want to quickly understand this site's relevance to me, so I don't waste my time on useless engagement 


### UX Design Scope User Requirements and Expectations
<br>
From the analysis of existing financial literacy/informational websites geared towards Ireland, a set of possible requirements was identified for a new portal.
<br>
The basic requirement is to provide a meta-portal which allows theme-based grouping of financial literacy resources.
<br>    
<ul>MVP Requirements:
<li>Must be intuitive to use</li>
<li>Must be easy to learn</li>
<li>Good for first time or returning users</li>
<li>Accessible - no ad display & no paywall</li>
<li>Easy visbility of financial themes</li>
<li> with ability to identify 'favourite' themes of interest and to hide themes not of interest (perhaps by have a 'my interests' page first and the main selection page second for returning users)</li>
</ul>
<br>
<ul>Requirements - Desirable:
<li>Should have administrator portal which allow for:</li>
<li>  creation of themes/ catgories, with title and brief descriptor</li>
<li>  ability to add resources to a theme, by resource type (link / tool / article/ blog post/ video clip)</li>
<li> Ability to assign estimated reading time</li>
  <li> ability to add one resoure to multiple themese?  Maybe using hashtags? </li>
  
<li>From a user perspective, should-haves and nice to haves include </li>li>
<li> Ability to filter content to just items/articles of interest</li>
<li> Distinguish between first time and returning user</li>li>
<li> Ability to browse annonymously and only create a profile once trust has been established </li>li>
<li> Guarantee of no ads or mis-use of information </li>li>
<li> cookie-free? </li>
<li> Ability to judge authenticity of informatio (possibly by upvotes?)</li>
<li> Ability to comment? </li>li>
<li> Ability to browse FAQ within a theme or topiic
</ul>
<br>
