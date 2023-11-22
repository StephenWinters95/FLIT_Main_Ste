# Financial Planner 
(Developer:  Deirdre McCarthy, Nov 2023)
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
R = Read
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
It shows the site branding to the left hand side, the site name to centre, a welcome message & Avatar/chosen profile photo for logged-in users.
Page links are for MyPlanner dashboard, About and Logout.   
![Navbar-registered user](./django_financial_planner/docs/readme_images/f02-navbar-registered-usr.png?raw=true "Navbar reflecting logged in user")

For first-time users in browsing mode the navigation bar doesn't show a personalised welcome message, and the menu options are different.
Particularly, no 'My Planner' option as an unregistered user doesnt have access to this feature.
![Navbar-unregistered user](./django_financial_planner/docs/readme_images/f02-unregistered-user.png?raw=true "Navbar reflecting first-time or casual user")

* Pagination of article content:
  
In order to make the site more usable, and to speed up page load times, the number of articles which load at once is currently set to 4; this may increase or decrease as the site matures.
Page back/ page forward buttons appear below the article summaries.

![Current & next paging through content](./django_financial_planner/docs/readme_images/f01-site-nav-pagination.png?raw=true "Pagination of content")

* Icons:
   
Certain icons and button styles appear consistently within the site, and their appearance may vary according to the user's security level.  

* For an unregistered user, or from the article summary screen, the 'like' icon shows in grey (this user is not authorised to 'like' articles).

* For a logged-in user, who hasn't yet liked this particular article, it will appear in the article detail window as red outline.
![like button](./django_financial_planner/docs/readme_images/f02-like-button.png?raw=true "Like button -- not activated")  

* For a logged-in user who has already liked the article, it will show as red solid.
Similarly, an activated bookmarks button (solid icon), means the current user added this article to their reading list.
![bookmarks button](./django_financial_planner/docs/readme_images/f02-bookmark-button.png?raw=true "Bookmark button -- activated")  

Clicking on the icon allows a logged-in user to toggle status on likes and bookmarks.

* Totals:
  
The button totals can be seen in different contexts.  Likes, bookmarks, comments, tasks are each represented by logos.
If viewed on article summary (home page) or article detail, they show totals from the article perspective.
If viewed on the user's dashboard, the totals relate to the user's activity, ie how many tasks does this user have, how many articles on thir reading list, how many article Responses have they left, and how any articles have they liked.

![User's MyPlanner dashboard](./django_financial_planner/docs/readme_images/f02-user-button-totals.png?raw=true "User's MyPlanner dashboard")  

So, the symbology remains the same but the count varies by context.

* Buttons:
  
Where possible the principle of progresive reveal is followed.  With the awareness that this is a content-heavy site, the user can reveal or hide certain information - such as Article Responses (comments), Article Tasks, and Reading Lists.
For example, Responses will default to hidden, but the user can see they exist on an Article, or on a user's MyPlanner dashboard:

![responses button](./django_financial_planner/docs/readme_images/f02-responses-icon.png?raw=true "Responses icon showing total")

Clicking on that button shows the expanded view of Responses ![responses](./django_financial_planner/docs/readme_images/f11-responses-expanded-from-button.png?raw=true "Responses detail pane")

The button toggles to ![hide responses](./django_financial_planner/docs/readme_images/f02-responses-button-toggle.png?raw=true "Responses toggle")

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

![consistent UX](./django_financial_planner/docs/readme_images/f03-consistent-ux.png?raw=true "consistent UX")

![consistent UX - errors](./django_financial_planner/docs/readme_images/f03-consistent-ux-errors.png?raw=true "consistent UX - errors")

![consistent UX - message login](./django_financial_planner/docs/readme_images/f03-consistent-ux-messaging-login.png?raw=true "consistent UX - message-login")

![consistent UX - message logout](./django_financial_planner/docs/readme_images/f03-consistent-ux-messaging-logout.png?raw=true "consistent UX - message-logout")

Meaningful Error messges
Confirmation messages (Feedback) when Create-Update-Delete actions are taken 

* SO_04 As site owner I want to provide straightforward, intuitive, consistent website navigation, (using graphical navigation where possible, even where the destination leads to text-based informataion)
* SO_06 As site owner I want to provide a website, which meets current programming, performance and accessibility standards (html, css, javascript, responsive, accessibility, performance)
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 
* FTU_06 As a first-time user I want clear, timely and unambiguous feedback and interaction
* FTU_07 As a first-time user I expect links and functions that work as expected

### F04 Responsive
The site is responsive and will re-draw based on the viewing device type, so can be used on a range of convenient devices.

This meets user requirments as follows:
* SO_04 As site owner I want to provide straightforward, intuitive, consistent website navigation, (using graphical navigation where possible, even where the destination leads to text-based informataion)
* SO_06 As site owner I want to provide a website, which meets current programming, performance and accessibility standards (html, css, javascript, responsive, accessibility, performance)
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 

### F05 About Page
![About page](./django_financial_planner/docs/readme_images/f05-about-page.png?raw=true "about page")

As the site developed it was realised that the site's 'About' page, while delivered as part of the functionality, is redudat becuase of the nature of this site - I think if would be preferable to add content that describes the site's purpose and to refer the user to that. rather than providing a static programmer-developed page.  The site admministrator can quite easily update and refresh article content, and this is actually a better approach.  To that end, several relevant articles have been created, these have all been associated with a tag of 'FinancialPlanner - About' so they can be retrieved from the LifeStage search.

* FTU_04 As a first time user I would like to understand the acountability and trustability of information presented on the site - maybe via an 
about page which clearly identifies information souces, information gathering/harvesting processes including moderation (flowchart would be good here).

### F06 Article Search/ Filter
On the article libary page, article search terms can be used to hone in on topics of interest.  This is easy to use by entering a word or term into the search box and taking the search button.  Articles which contain that search term within their **body content** will be shown on the homepage and the user can browse as normal.  To clear the search, either enter blank in the search term and press Search, or use the Home button to return.
This type of search is very useful for unstructured searching.

![article search - result](./django_financial_planner/docs/readme_images/f06-article-search-result.png?raw=true "Article search - result")

* SO_05 As site owner I want to allow users to 'chop and dice' complex information into small chunks 
* FTU_01 As a first time user I want to access relevant information to increase my financial understanding/literacy on a specific topic
* FTU_02 As a first-time user I about what this site does, and want to quickly understand this site's relevance to me, so I don't waste my time on useless engagement 
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 


### F07 Lifestage filter
A second type of search - a Lifestage filter - is available.  This allows searching for articles associated with a pre-defined theme.
These pre-defined themes are defined as 'tags' in the FinancialPlanner Administrator Console.

![lifestage tag maintnance](./django_financial_planner/docs/readme_images/f07-lifestage-filter-article-tags.png?raw=true "Article tags")

Tags are associated with articles, and there are two ways to update the assocation.  The first is to edit the tag field within the article and add the tag name within quotes, e.g. "Plan for Care in Later Life".  However this method is not ideal, as the field in the Admin Console is unvalidated and allows for free-format text entry.  If a search term is not exactly specified then a categorised article may not be retrieved as expected within Financial Planner.

A better way is to maintain from the tag perspective and to maintain a list of all articles associated with the tag.  Again this is not a perfect solution as the adminstrator must determine the ObjectID of each article, however it suffices at this time for proof-of-concept, and it ensures that the correct association is definitely made.  

![lifestage tag-article maintnance2](./django_financial_planner/docs/readme_images/f07-lifestage-filter-linking-tag-to-article2.png?raw=true "Article linking to tags")

Adding an article to a tagged list performs the corresponding update to the Article's 'Tags' field.

![lifestage tag-article maintnance](./django_financial_planner/docs/readme_images/f07-lifestage-filter-linking-tag-to-article.png?raw=true "Article linking to tags")

This addresses user stories:
* SO_05 As site owner I want to allow users to 'chop and dice' complex information into small chunks 
* FTU_01 As a first time user I want to access relevant information to increase my financial understanding/literacy on a specific topic
* FTU_02 As a first-time user I about what this site does, and want to quickly understand this site's relevance to me, so I don't waste my time on useless engagement 
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 

### F08 Article Library
The full set of articles is available from the Articles link on the navigation bar. 
From this screen the user can see article title, image suggestive of content, summary/ excerpt, author, last updated, and gain an idea of article popularity, by seeing the number of likes, bookmarks and comments for the article.   'New' articles are flagged.

![Homepage](./django_financial_planner/docs/readme_images/f08-article-library.png?raw=true "Article library")

* SO_01 As site owner I want to provide a platform where users can directly access useful resources to help with real-life financial decision making
* SO_02 As site owner I want to largely (but not entirely) re-use/ connect to information from authoritative sources 
* SO_03 As site owner I want to avoid connecting to information which is opinion- rather than fact-based (ie perhaps from a less authoritative source) or at least highlight that the source is less authorative, or offered by a biased source.
* FTU_01 As a first time user I want to access relevant information to increase my financial understanding/literacy on a specific topic
* FTU_02 As a first-time user I about what this site does, and want to quickly understand this site's relevance to me, so I don't waste my time on useless engagement 
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 

### F09 Article Details
Article details may include infographics, text, in-frame video.  Text is set at a readable font size.

![Article activity bar](./django_financial_planner/docs/readme_images/f09-activity-bar.png?raw=true "Article activity bar ex2")

![Article content](./django_financial_planner/docs/readme_images/f09-article-content.png?raw=true "Article content")

Articles can, thanks to the Summernote Django add-in, contain a variety of content.  For example the article below holds a 2-column table with an infographic to the left and article text to the right. 
![Article content showing links and infographic](./django_financial_planner/docs/readme_images/f09-article-content-ex1.png?raw=true "Article content with infographic and links")

In-frame video from certain providers (YouTuve, Veemo, and others) is also supported which gives a rich user experience.  For example, the article below contains a clip from the RTE 'How to be Good with Money' TV Series, with content funded by the Irish Competition & Consumer Protection body.

![Article content with video](./django_financial_planner/docs/readme_images/f09-article-content-ex2.png?raw=true "Article content with video clip")

![Article content zoom out](./django_financial_planner/docs/readme_images/f09-article-content-zoom-out.png?raw=true "Article content - zoom out")


* SO_01 As site owner I want to provide a platform where users can directly access useful resources to help with real-life financial decision making
* SO_02 As site owner I want to largely (but not entirely) re-use/ connect to information from authoritative sources 
* SO_03 As site owner I want to avoid connecting to information which is opinion- rather than fact-based (ie perhaps from a less authoritative source) or at least highlight that the source is less authorative, or offered by a biased source.

### F10 Tasks
Articles may contain one more suggested tasks.  Often these will include a link, either to a site where the user needs to take a follow-on activity.  These could be:
- a URL connecting to a government website e.g. the Irish Revenue site
- a link to a Google sheet which can be personalised e.g. household budget 

![Article tasks](./django_financial_planner/docs/readme_images/f10-article-tasks.png?raw=true "Article tasks")

Registered users have the option to copy individual tasks to a personal task tracker.  
For registered users, a 'copy' icon is seen beside each action 
* SO_11 As site owner, I would like to encourague users to engage with each article's content, by providing suggested actions and next steps for the user to take 
* FTU_06 As a first-time user I want clear, timely and unambiguous feedback and interaction
* FTU_07 As a first-time user I expect links and functions that work as expected

### F11 Article Responses
a.k.a. comments

![Article responses example](./django_financial_planner/docs/readme_images/f11-responses-expanded-from-button.png?raw=true "Responses")

* SO_11 As site owner, I would like to encourague users to engage with each article's content, by providing suggested actions and next steps for the user to take 

### F12 Reading List
ability for a registered user to add an article to their reading list:

![Reading list (bookmarks)](./django_financial_planner/docs/readme_images/f12-reading-list.png?raw=true "Reading List")

* SO_11 As site owner, I would like to encourague users to engage with each article's content, by providing suggested actions and next steps for the user to take 
* RU_01 As a returning user I want to mark information I find useful so I can quickly access it again (favourites)
* RU_02 As a returning user I want to create a user profile so that I can personalise my site experience (profile image, bookmarks, actions/tasks)

### F13 Personalised tasks - MyPlanner
Personalised view.
From where personal tasks may be created, edited, or deleted.
The users reading list can also be shown.
As can the comments they've made on various articles.
![My Planner](./django_financial_planner/docs/readme_images/f13-personalised-view-myplanner.png?raw=true "MyPlanner")

Progressive reveal is used to hide information until the user requests it.
Possible to maintain and edit personal tasks from here.

* SO_12 As site owner, I would like to provide a personal database where users can store their own actions and record their progress in following the steps
* RU_01 As a returning user I want to mark information I find useful so I can quickly access it again (favourites)
* RU_02 As a returning user I want to create a user profile so that I can personalise my site experience (profile image, bookmarks, actions)

### F14 My Tasks

* CREATE A USER TASK:
A logged-in user can create a 'task' that is, a structured activity which is prompted by an article they have read.  A user task can be created either by copying an article task (the preferred method) or by direct keying of a new task.  Once the task is created, if can be accessed from the task list on the 'My Planner' dashboard, and can be edited, or indeed deleted, by the user.  
  
* READ TASKS:
On the MyPlanner dashboard, the number of tasks created by this user is shown, and can be hidden or revealed by the 'Show Tasks' button.

See user's task list.  Task 30 is selected for edit.  
![Personal Tasks](./django_financial_planner/docs/readme_images/f14-my-tasks.png?raw=true "My Tasks")

* UPDATE TASKS:
An update panel is given, and the user updates the 'Progress' field
![Personal Tasks - update](./django_financial_planner/docs/readme_images/f14-my-tasks-update.png?raw=true "My Tasks - update")

Press the Submit button.
A confirmation message is shown to confirm the update:
![Personal Tasks - update confirm](./django_financial_planner/docs/readme_images/f14-my-tasks-update-message.png?raw=true "My Tasks - update confirmed")

The update can be seen when the user's task list is re-displayed:
![Personal Tasks - updated](./django_financial_planner/docs/readme_images/f14-my-tasks-updated.png?raw=true "My Tasks - updated")


* DELETE TASK:
To delete a task, select the red 'bin' icon on the grid. Task 30 is now selected for delete:
![Personal Tasks - delete confirm](./django_financial_planner/docs/readme_images/f14-my-tasks-confirm-delete.png?raw=true "Confirm delete")

A confirmation message appears, the total number of tasks is decremented, the task no longer shows on the task list
![Personal Tasks - delete confirmed](./django_financial_planner/docs/readme_images/f14-my-tasks-confirmed-delete-and-total-decremented.png?raw=true "Confirmed delete")


### F15 Content Manaagement (Current and FUTURE)
Done by an administrator (a user flagged as 'staff') using the application back-end.

As the application has grown, this interface has increased in complexity.  It currently looks like this:
![Content Mgt overview](./django_financial_planner/docs/readme_images/f15-content-management-overview.png?raw=true "Content Mgt")

This administration portal has been adequate as a proof-of-concept whilst delivering the Finance Planner application.
However as number of articles increase, so does the maintenance overhead.  
The process for adding a new article is now:
* Create draft article with appropriate imagery and content
* Review the lifestage tags to determine which (if any) are most appropriate
* Either append "exact lifestage text" to the article tags; or update the tag table with the article primary key record #.
* Create any tasks (article actions) needed for the article and link them to the parent article.

As a next development step for the FinancialPlanner app, I would highly recommend developing an admin portal.  (FUTURE REQUIREMENT) 
This would allow an Article and each of its related elements to be maintained in sync.  This wasn't intially a requirement as the standard Django-delivered Admin Console was considered adequate, however the data complexity and maintenance overhead have increased as the site has neared completion, and data has been added.  

### F16 Content Management - Article Creation

The main elements of an article which are needed for creation are:
title, excerpt, body of article.
Through using summernote, there is reasonable editorial flexibility in creating article content.  
In the example below, an infographic was created usng Canva, and the summernote form was setup with a 2-colum table structure.
The infographic was inserted in the leftmost column and the text to the right.

![Content Mgt detail](./django_financial_planner/docs/readme_images/f16-article-maintenance-content.png?raw=true "Content Mgt - detail")

With initial user testing, users had some difficulty reading screen content, therefore the best approach seems to be Arial-16 font 
(the number of fonts available within SummerNote is not extensive), with minimal tetx and good use of graphics or pictorial elements.
Note that summernote supports in-frame video from a range of providers, e.g. it was possible to use Veemo video links to embed some of the CCPC 
(consumer protection council of Ireland)'s video from the RTE 'how to be good with money' series. 



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
