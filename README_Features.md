# Financial Planner 
(Developer:  Deirdre McCarthy, Nov 2023)

# Features within the Financial Planner App:
1. [Intro](#introduction)
2. [Project Goals: ](#project-goals)
    1. [UX Design - Strategy ](#ux-design-strategy) 
    2. [UX Design - Strategy - Competitor Portals](#ux-design-strategy-analysis-of-competitors)
    3. [UX Design - Strategy - Target Audience](#ux-design-strategy-target-audience)
3. [UX Design - Scope](#ux-design-scope)
    1. [UX Design - Scope - User Requirements and Expectations](#ux-design-scope-user-requirements-and-expectations)
    2. [UX Design - Scope - Data](#ux-design-scope-data)
    3. [UX Design - Scope - Viewing Device](#ux-design-scope-viewing-device)
4. [User goals/ user stories: ](#user-goals-user-stories)
    1. [Site Owner Goals](#site-owner-goals)
    2. [First-time User Goals](#first-time-user-goals)
    3. [Returning User Goals](#returning-user-goals)
    4. [Other stakeholder Goals](#other-stakeholder-goals)
5. [Further UX Design: ](#ux-design-decisions)
    1. [Skeleton - Wireframes; ](#wireframes)
    2. [Surface - Fonts; ](#fonts-chosen)
    3. [Surface - Colours](#colour-scheme)
    4. [Surface - Imagery](#design-images)
6. [Features](#features)
    1. [Included](#features-in-scope)
    2. [Future Development](#features-left-to-implement)
8. 
## Introduction
---------
Financial Planner offers a portal for financial education content, with information relevant to the republic of Ireland.

It acts as a virtual assistant to empower users navigating financial decision making.
By making complex tasks clearer; 
and by identifying useful resources and online contacts.

Users are empowered.

Observation that seemingly small decisions taken at various life stages can have large consequences through out life.
Lots of individual useful websites but you need to work hard to link together the information.
Difficult to get information specifically dealing with Irish government revenue and rules.

And abilty for the user to pickup content which is relevant to their needs.
  
Therefore, the gap to be adressed is navigational.... how does a user find information relevant to their needs? 
People are being increasingly directed towards self-learning.

But this is challenging because of the huge diversity of information sources and resources.

This **first** release of the Financial Planner portal is aimed at:

a. Individuals (rather than companies or organisations)<br>
b. Who have financial agency (decision-making capacity)
c. who reside or operate within the financial and legal boundaries of the Republic of Ireland (as financial content is specific to this territory)
d. who are at various adult life stages (18 -> end of life) 
e. who have internet access and the capacity to navigate a website
f. with the ability to read engish-language content (some of the content may be translatable e.g. using Google translate, but this cannot be assumed or taken for granted)
g. who wish to understand what financial information is relevant and important to a particular life stage/event.

This website includes 3 pages and 16 features 
The pages - which effectively bring the features lited in the previous section together - are:
* Landing Page (see feature F01 Intro Screen)
* Settings page (see feature F16 Feedback and settings )
* 404 error page 

<details><summary></summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/"></details>

- __404 Error Page__ 
This allows graceful failure, where the header and footer are preserved, allowing the user to navigate away from an error page using the site navigation (rather than the back button).


## Features
----------------

### F01 Site Navigation
A consistent navigation bar is shown at the top of ach screen.  It shows the site logo to the left hand side, the site name to centre, a user Avatar logo and welcome message for logged-in users, and page links to the right hand side.   

For first-time users in browsing mode the navigation bar looks like this:


For returning users who have registered on the site the navigation bar is personalised with the user's name and profile photo/chosen Avatar.  The options to the right-hand-side now include 'My Planner' link and 'Logout' rather than 'Login'.

For returning users who have created a profile, the navigation bar looks like this:

* SO_04 As site owner I want to provide straightforward, intuitive, consistent website navigation, (using graphical navigation where possible, even where the destination leads to text-based informataion)
* SO_06 As site owner I want to provide a website, which meets current programming, performance and accessibility standards (html, css, javascript, responsive, accessibility, performance)
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 
* FTU_07 As a first-time user I expect links and functions that work as expected


### F02 Consistency.
The User Experience is designed to be consistent across the app.
Certain logos and button styles appear consistently within the site (need table style markdown here)
* likes:  XX as seen by an unregistered user; XX as seen by a registered user; XX activated by registered user (article detail view)
* Reading list:  YY unregistered user YY registered YY activated. 
* Tasks : 

Submit button
Cancel link

Copy icon
Edit icon

'view'/'hide' toggle buttons
Some screens follow the concept of progressive reveal, where summary information is shown and the user can click to see more.  
An example is the 'My Planner' screen for registered users, 

* SO_04 As site owner I want to provide straightforward, intuitive, consistent website navigation, (using graphical navigation where possible, even where the destination leads to text-based informataion)
* SO_06 As site owner I want to provide a website, which meets current programming, performance and accessibility standards (html, css, javascript, responsive, accessibility, performance)
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 
* FTU_06 As a first-time user I want clear, timely and unambiguous feedback and interaction
* FTU_07 As a first-time user I expect links and functions that work as expected

### F03 Responsive
The site is responsive and will re-draw based on the viewing device type, so can be used on a range of convenient devices.


User stories XYZW are satisfied by features F01..F03, and the aim is to make using this site easy to learn with predictable, reliable navigation.

* SO_04 As site owner I want to provide straightforward, intuitive, consistent website navigation, (using graphical navigation where possible, even where the destination leads to text-based informataion)
* SO_06 As site owner I want to provide a website, which meets current programming, performance and accessibility standards (html, css, javascript, responsive, accessibility, performance)
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 

### F04 Site security
Based on the user's registration status and security level, they can access varying levels of site features:
(table needed here)
unregistered/ first time user   can browse site, view articles and access article links
user profile created            user can like, bookmark, create personal tasks
photo added to user profile     avatar appears on site navbar and certain features (e.g. article responses)
staff user                      access to backend; can create draft/published articles, maintain article tags, actions.  User profile, user data maintenance.  

* FTU_06 As a first-time user I want clear, timely and unambiguous feedback and interaction
* FTU_07 As a first-time user I expect links and functions that work as expected

### F05 Lifestage filter
On first accessing the app, the lifestage link is shown.  This allows anyone to search based on themes, and to retrieve financial guidance articles relevant to that theme.

* SO_05 As site owner I want to allow users to 'chop and dice' complex information into small chunks 
* FTU_01 As a first time user I want to access relevant information to increase my financial understanding/literacy on a specific topic
* FTU_02 As a first-time user I about what this site does, and want to quickly understand this site's relevance to me, so I don't waste my time on useless engagement 
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 

### F06 Article Search/ Filter
On the article libary page, article tags can be used to hone in on topics of interest.

* SO_05 As site owner I want to allow users to 'chop and dice' complex information into small chunks 
* FTU_01 As a first time user I want to access relevant information to increase my financial understanding/literacy on a specific topic
* FTU_02 As a first-time user I about what this site does, and want to quickly understand this site's relevance to me, so I don't waste my time on useless engagement 
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 

### F07 Article Library
The full set of articles is available from the Articles link on the navigation bar. 
From this screen the user can see article title, image suggestive of content, summary/ excerpt, author, last updated, and gain an idea of article popularity, by seeing the number of likes, bookmarks and comments for the article.   'New' articles are flagged.

* SO_01 As site owner I want to provide a platform where users can directly access useful resources to help with real-life financial decision making
* SO_02 As site owner I want to largely (but not entirely) re-use/ connect to information from authoritative sources 
* SO_03 As site owner I want to avoid connecting to information which is opinion- rather than fact-based (ie perhaps from a less authoritative source) or at least highlight that the source is less authorative, or offered by a biased source.
* FTU_01 As a first time user I want to access relevant information to increase my financial understanding/literacy on a specific topic
* FTU_02 As a first-time user I about what this site does, and want to quickly understand this site's relevance to me, so I don't waste my time on useless engagement 
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 

### F08 Article Details
Article details may include infographics, text, in-frame video.  Text is set at a readable font size.

* SO_01 As site owner I want to provide a platform where users can directly access useful resources to help with real-life financial decision making
* SO_02 As site owner I want to largely (but not entirely) re-use/ connect to information from authoritative sources 
* SO_03 As site owner I want to avoid connecting to information which is opinion- rather than fact-based (ie perhaps from a less authoritative source) or at least highlight that the source is less authorative, or offered by a biased source.

### F09 Tasks
Articles may contain one more suggested tasks.  Often these will include a link, either to a site where the user needs to take a follow-on activity.  These could be:
- a URL connecting to a government website e.g. the Irish Revenue site
- a link to a Google sheet which can be personalised e.g. household budget 

Registered users have the option to copy individual tasks to a personal task tracker.  
For registered users, a 'copy' icon is seen beside each action 
* SO_11 As site owner, I would like to encourague users to engage with each article's content, by providing suggested actions and next steps for the user to take 
* FTU_06 As a first-time user I want clear, timely and unambiguous feedback and interaction
* FTU_07 As a first-time user I expect links and functions that work as expected


### F10 Article Responses
a.k.a. comments
* SO_11 As site owner, I would like to encourague users to engage with each article's content, by providing suggested actions and next steps for the user to take 

### F11 Reading List
ability for a registered user to add an article to their reading list
* SO_11 As site owner, I would like to encourague users to engage with each article's content, by providing suggested actions and next steps for the user to take 
* RU_01 As a returning user I want to mark information I find useful so I can quickly access it again (favourites)
* RU_02 As a returning user I want to create a user profile so that I can personalise my site experience (profile image, bookmarks, actions/tasks)

### F12 MyPlanner
Personalised view.
From where personal tasks may be created, edited, or deleted.
The users reading list can also be shown.
As can the comments they've made on various articles.

Progressive reveal is used to hide information until the user requests it.
Possible to maintain and edit personal tasks from here.

* SO_12 As site owner, I would like to provide a personal database where users can store their own actions and record their progress in following the steps
* RU_01 As a returning user I want to mark information I find useful so I can quickly access it again (favourites)
* RU_02 As a returning user I want to create a user profile so that I can personalise my site experience (profile image, bookmarks, actions)

### F13 About Page
* FTU_04 As a first time user I would like to understand the acountability and trustability of information presented on the site - maybe via an 
about page which clearly identifies information souces, information gathering/harvesting processes including moderation (flowchart would be good here).


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




### Syste Owner/Operator Goals
* SO_13 As site owner, I would like to make the content of the database shareable and reusable to others (perhaps subject to signing a re-use agreement) by providing an API to the published database (FUTURE)

### First-time User Goals
* FTU_08 (FUTURE) As a first time user I would like to understand the part I can play in contributing to the body of knowledge

### Returning User Goals
* RU_03 As a returning user want to build my knowledge in certain areas
* RU_04 As a returning user I want to build the body of knowledge for other users (by adding likes and article Responses).
* RU_05 As a returning user I want to personalise my experience
* RU_06 As a returning user I want practical steps and tasks, and to be able to apply the site knowledge to my own experience (personalised actions)
* RU_07 As a returning user I 
* RU_08 (FUTURE) As a returning user I 
* RU_09 (FUTURE) As a returning user I 
* RU_10 (FUTURE) As a returning user I 

### Other stakeholder Goals
* OT_01 As an educator I  
* OT_02 As The Department of Finance Ireland I want to use this site towards achieving financial literaccy objectives and address the deficit identified in report XXXXX of 20XX.









### ### Financial_Planner site Ethos & Values:
* Integrity: - <br>
Commencing an Internet search for Financial Planning advice, is akin to entering a tropical sea infested with sharks.  For the unwary, vulnerable or less knowledgable user, exposing their personal details (by initiating tracked searches on cookie-infested sites, searching for particular information or creating a user account) can have the same effect as bloodletting into the shark-infested waters, attracting predators who seek to target and exploit vulnerabilities.  When seeking information, it can be difficult to differentiate between opinions and fact.<br>
More sophisticated users can be fearful of exposure to these sharks, and more vulnerable users may avoid information seeking due to fear.

### Financial_Planner site authenticity - <br>
Acting as a trusted source that offers reliable information to users - is paramount.  Financial_Planner must be a trusted source that offers reliable, verifiable information to users.<br>
*  Information autenticity - information is primarily to be sourced from verifiable sources (primarily government or educational resources)
*  Users are to be able to indicate individual content relevance (likes & shares)
*  ??? User comments, actively moderated before publishing, may be permitted in a future release - however there is a risk of thereby introducing opinion-based content ???

### Financial_Planner site integrity -<br> 
The user is offered a tracking-free experience (errr check if this is actually a real possibility)
*  The user is guaranteed that their information will not be redistributed, re-used elsewhere or otherwise by the site owners or moderators.
*  The site owners apply appropriate methods to protect user registration information from hacking and security vulerabilities.
*  (FUTURE) In the future, the Financial_Planner site would dearly like to offer financial calculators into which users could enter some of their financial decisions and receive feedback and guidance..maybe about opportunities they could take at different life stages to improve their financial control for present & future needs..ideally as a game-based interface...but need to be cautious as, if users enter their financial details and save to a shared portal, will they then become vulnerable to someone hacking their information?
<br>     

### User Empowerment
A key objective of the Financial_Planner site is to make good-quality information readily available to users who wish to improve their financial awareness and decision-making.
That is, to empower users to become aware of financial dimensions of decision-making
Sites exist which are information-rich, however the information is 'buried' in a myriad of state portals.
In designing the site, then, particular emphasis is placed on accessibility, navigability and ability to retrieve relevant information.  In many cases, making <br>
<br>
<br>

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
