# Financial Planner 
(Developer:  Deirdre McCarthy, Nov 2023)

# Table of Contents:
1. [About](#about)
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
6. [Agile Methology: ](#agile)
    1. [Project setup](#project)
    2. [Designing an Issue Template](#issue-template)
    3. [Creating project issues](#project-issues)
    4. [EPICs ](#epics)
    5. [MoSCoW Prioritisation;](#moscow-prioritisation)
    6. [Level of Effort estimation - Story Points](#story-points)
    7. [Project Milestones](#milestones)
    8. [Project Sprints](#sprints-and-iterations)
    9. [Issue Lifecycle](#issue-lifecycle)
    10. [Project tabular view](#tabular-projects-view)
    11. [Kanban board](#kanban-board)
    12. [Observations and learnings](#agile-observations-and-learnings)    
7. [Features](#features)
    1. [Included](#features-in-scope)
    2. [Future Development](#features-left-to-implement)
8. [Technology](#technologies)
    1. [Languages](#langugages)
    2. [Frameworks and Tools](#frameworks--tools)
9. [Validation](#validation)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Javascript Validation](#javascript-validation)
    4. [Accessibility](#accessibility)
    5. [Performance](#performance)
    6. [Multi-device Testing](#multi-device-testing)
    7. [Multi-browser Testing](#multi-browser-testing)
    8. [Testing user stories](#testing-user-stories)
    9. [Unfixed Bugs](#unfixed-bugs)
10. [Accessibility](#accessibility)
11. [Performance](#performance)
12. [Deployment](#deployment)
13. [Credits](#credits)
    1. [Content](#content)
    2. [Media](#media)
    3. [Code](#code)
    4. [References](#references)
    5. [Acknowledgements](#acknowledgements)

## About
---------
Financial Planner is a system which aims to address the recognised gaps in financial literacy within Southern Irish society.
Background statement of problem.
Department of Finance initiatives commenced with survey of practitioners Sept 2023.
Life experience of the developer, extensive reading and personal interest in the FIRE (Financial Independence Retire Early) community.
Observation that seemingly small decisions taken at various life stages can have large consequences through out life.
<br>
Observaton that there are multiple sites in existence which address elements of financial planning, but a limited offering for whole-of-life planning, from cradle to grave  <br>
Lots of individual useful websites but you need to work hard to link together the information.
Difficult to get information specifically dealing with Irish government revenue and rules.

<br>
Ideally, by the time development is completed, this site will include:
* life stage-themed links to useful information
* content and theme management
* ability for users to personalise their site experience by marking resources (articles and links) of interest as favourites, which are highlighted on their return (similar to bookmarks)
* quiz?  confirmation of understanding?  Might be a bit patronising?  who the 
* would absolutely love to have a game which takes the user from age 0 to their resting age and allows them to visualise the consequences of financial decisions
   
### Responsive Mockup
https://ui.dev/amiresponsive?url=https://deemccart.github.io/CI_PP4_FinancePlanner/

### Live webpage link
https://deemccart.github.io/CI_PP4_Financial_Planner

## Project Goals
----------------
1. To provide a portal for financial education content. 
2. Initially loaded with information relevant to the republic of Ireland.
3. Can be Organised into themes (life Stages) defined by an adminstrator.
4. Can allow content to be stored and classified including links, videos.
5. Where the user can tag items of interest/ further refernce.   
6. Which uses the capabilities of Django, HTML, CSS and Javascript.
7. And is accessible, responsive and relevant.
  
### UX Design Strategy
To be described.
But focus is on accessible content, for the naive or more sophisticated user.
And abilty for the user to pickup content which is relevant to their needs.


### UX Design Strategy Analysis of Competitors
Competitor/ similar site analysis was undertaken over a two-week period during September 2023 to analyse existing financial literacy education schemes and information resources, the target audience for same, and to identify gaps which might provide opportunities for a new solution.
The research methodology was initially Google searches (ideally to be followed up by user interviews with thought leaders in the area of financial literacy education).

Financial literarcy Content is, in many cases, rich, detailed and valualable.
Government-funded websites such as CCPC, Citizens advice, Revenue offer clear and authoritive advice, and it is possible to determine when the advice was last updated.
Consumer-led sites such as switcher.ie, bonkers.ie, cheapestoil.ie offer comparisons of specific services or products (electricity supplier, telecomms providers, fuel prices) . 
However it is also quite dispersed, and topic searches can require considerable persistence to obtain a full picture.
Truth verification can be difficult, opinion-based sources can appear to hold equal weight with authoritiative sources.  
Vulnerable users researching can fall prey to information-gathering websites which then seek to market or target the customers for revenue-earning purposes, often recycling the customers own information as part of this exercise.
Financial literacy programmes are taking shape in schools, however there does not seem to be entire-life financial educational focus
Bank of Ireland in ther consumer study of XXXXXX, observed that many middle-class parents will gift their children, not only with financial resources, but with the knowledge and learning of how to manage and maintain these resources.
People raised in humble circumstances neither benefit from inherited wealth, nor typically do they absorb this detailed knowledge within their home environment. 
Retail banks, who traditionally prospered through relationship marketing, have since c. 2012 retreated into transactional processing, which reduces the opportunity for customers to learn from conversations with bank staff.  
Post offices, offered as an alternative, are primarily transaction focussed, and reply on unqualified staff who can provide limited financial guidance to customers.
People are being increasingly directed towards self-learning.

But this is challenging because of the huge diversity of information sources and resources.

Therefore, the gap to be adressed is navigational.... how does a user find information relevant to their needs? 
.
List of websites/pages analysed includes:
..... to be listed here .......


<details><summary>Summary of findings</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/django_financial_planner/docs/readme_images/strategy_competitive_analysis.jpg"></details>

### UX Design Strategy Target Audience
This **first** release of the Financial Planner portal is aimed at:

a. Individuals (rather than companies or organisations)<br>
b. Who have financial agency (decision-making capacity)
c. who reside or operate within the financial and legal boundaries of the Republic of Ireland (as financial content is specific to this territory)
d. who are at various adult life stages (18 -> end of life) 
3. who have internet access and the capacity to navigate a website
f. with the ability to read engish-language content (some of the content may be translatable e.g. using Google translate, but this cannot be assumed or taken for granted)
g. who wish to understand what financial information is relevant and important to a particular life stage/event.

## UX Design Scope
----------------
### Financial_Planner site Ethos & Values:
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
<li> Ability to browse FAQ within a theme or topic? </li>


<li>bility to </li>Would like to be able to track user statistics (cookies)</li>
<li>Would like to be able to auto-generate new equations</li>
<li>Would like to be able to track equations already used</li>
<li>Would like to be able to set difficulty levels</li>
</ul>
<br>
<ul>To incorporate as many of the Wordle characteristics below as possible:
<li>Simple interface with uncluttered screen</li>
<li>clearly understood rules</li>
<li>scarcity - user can only access one game per day</li>
<li>reponsiveness - ability to play on small screens (convenient for user)</li>
<li>no time-out - can fit into small pockets of time as game will remain on-screen until 6 guesses completed</li>
<li>feedback and interaction - user immediately gets feedback for each guess</li>
<li>statistic tracking - user can track # of attempts to solve, number of days solved, success rates</li>
<li>peer-group communication - user can share their problem-solving pattern (without revealing any part of the solution) to friends who may also play</li>
</ul>

### UX Design Scope - Data
Initial themes loaded and displayed will be based on ROI (Republic of Ireland) datasets

## User Goals/ User Stories
----------------
Written in the format 'As a **role** I want to **action** to achieve **desired outcome**    
### Site owner/moderator Goals
* SO_01 As site owner I want to provide a platform where users can directly access useful resources to help with real-life financial decision making
* SO_02 As site owner I want to largely (but not entirely) re-use/ connect to information from authoritative sources 
* SO_03 As site owner I want to avoid connecting to information which is opinion- rather than fact-based (ie perhaps from a less authoritative source) or at least highlight that the source is less authorative, or offered by a biased source.
* SO_04 As site owner I want to provide straightforward, intuitive, consistent website navigation, (using graphical navigation where possible, even where the destination leads to text-based informataion)
* SO_05 As site owner I want to allow users to 'chop and dice' complex information into small chunks 
* SO_06 As site owner I want to provide a website, which meets current programming, performance and accessibility standards (html, css, javascript, responsive, accessibility, performance)
* SO_07 As site owner I want to provide an opportunity for the user to provide feedback, including reporting issues, or suggesting improvements to the Financial Planner site
* SO-08 As site owner I want to acknowledge to the user that their feedback has been received
* SO-09 As site owner I would like to store a database of content to include url links, 
* SO-10 As site owner, I would like to have the capability to organise the content by lifestage, theme, and other criteria (possibly hierarchical groupings, hashtags) to allow cross referncing of user needs to content 
* SO_11 As site owner, I would like to encourague users to engage with each article's content, by providing suggested actions and next steps for the user to take 
* SO_12 As site owner, I would like to provide a personal database where users can store their own actions and record their progress in following the steps
* SO_13 As site owner, I would like to 
* SO_14 As site owner, I would like to make the content of the database shareable and reusable to others (perhaps subject to signing a re-use agreement) by providing an API to the published database)

### First-time User Goals
* FTU_01 As a first time user I want to access relevant information to increase my financial understanding/literacy on a specific topic
* FTU_02 As a first-time user I about what this site does, and want to quickly understand this site's relevance to me, so I don't waste my time on useless engagement 
* FTU_03 As a first time user I would like to be able to easily navigate the site and quickly learn its functionality 
* FTU_04 As a first time user I would like to understand the acountability and trustability of information presented on the site - maybe via an 
about page which clearly identifies information souces, information gathering/harvesting processes including moderation (flowchart would be good here).
* FTU_05  As a first-time user I would like to undertand the role of user feedback and user reviews 'X users found this useful or relevant',
* FTU_06 As a first-time user I want clear, timely and unambiguous feedback and interaction
* FTU_07 As a first-time user I expect links and functions that work as expected
* FTU_08 (FUTURE) As a first time user I would like to understand the part I can play in contributing to the body of knowledge


### Returning User Goals
* RU_01 As a returning user I want to mark information I find useful so I can quickly access it again (favourites)
* RU_02 As a returning user I want to create a user profile so that I can personalise my site experience (profile image, bookmarks, actions)
* RU_03 As a returning user want to build my knowledge in certain areas
* RU_04 As a returning user I want to build the body of knowledge for other users (by adding credibility ratings).
* RU_05 As a returning user I want to 
* RU_06 As a returning user I
* RU_07 As a returning user I 
* RU_08 (FUTURE) As a returning user I 
* RU_09 (FUTURE) As a returning user I 
* RU_10 (FUTURE) As a returning user I 

### Other stakeholder Goals
* OT_01 As an educator I  
* OT_02 As The Department of Finance Ireland I want to use this site towards achieving financial literaccy objectives and address the deficit identified in report XXXXX of 20XX.


## UX Design Decisions
----------------

### Wireframes
<details><summary>Landing Page - Articles</summary>
<img src="./django_financial_planner/docs/readme_images/wireframe-01-articles.png">
</details>

<details><summary>Lifestage Planner - themed access to Articles</summary>
<img src="./django_financial_planner/docs/readme_images/wireframe-02-themed-articles.png">
</details>

<details><summary>Article detail - with suggested actions</summary>
<img src="./django_financial_planner/docs/readme_images/wireframe03-article-detail.png">
</details>

<details><summary>My Planner - personalised user profile/action tracker</summary>
<img src="./django_financial_planner/docs/readme_images/wireframe04-my-planner.png">
</details>


<details><summary>About/ Feedback page</summary>
<img src="./django_financial_planner/docs/readme_images/wireframe05-about-feedback.png">
</details>
  
### Fonts Chosen
The fonts are deliberately chosen to mimic appearance of Wordle screen. 
In real life, Wordle uses proprietary fonts (NYT Karnak Condensed), with Helventica Sans for the grid and button text.  A reasonably close match, which is widely available on a range of devices, was thought to be the Google bebas Neue font.

However, when testing the site this did not present a good look, and so Roboto Slab was chosen as a better alternative.
Fallback fronts are used in both cases

### Colour Scheme 
The colour combinations mimic Wordle's game (for consistency and to ease the user learning experience).
   
The choice of colours for Financial Planner is very much in accordance with user stories S_02 (closely emulate the Wordle look & feel); FTU_02 (first-time user to easily navigate and learn the site) - consistent with Wordle so as to speed the learning process and encourage the focus on the game content, rather than on how to use it.

<details><summary>Colours- similar to Wordle</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/django_financial_planner/docs/readme_images/f07_game_grid_in_progress.jpg">
</details>

### Design Images
This site has very few images as the focus is on the game content.
A 'Wordle-type' logo is used on the Intro page.
<details><summary>'Wordle-type' logo</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/django_financial_planner/docs/readme_images/numble_icon.jpg">
</details>

### Design Images - Icons and Symbols

Certain icons and symbols (again based on Wordle look & feel) are used for quicklinks e.g. ? for About page, graphy symbol for Stats page, cog symbol for settings page. 


## Agile
An Agile approach was followed in plannning this project.  This is somewhat in contrast to the developer's well-practised 'waterfall' habits and presented both a challenge and an opportunity to think in a different way about deliverables and incremental delivery.
It was helpful that the developer participated in a hackathon during Sept 2023, and had an opportunity to observe experienced Agile developers, and their use of Github issue tracking in a team environment.
This led to a much clearer understanding of User story and task breakdown, as well as how github can be tailored  to add value, rather than overhead(!), to programming work.
* One precept which was difficult to master was respecting the timeboxing of each iteration.  Attempts to 'just finish' a task by extending the iteration by a day or two, needed to be curbed.  Instead, I had to (will have to) train myself to end the sprint, then assess which work had been completed or not.
* Story points present another challenge.  A very natural interpretation of story points is to assign them a time value (rather than an 'effort' value).  So, at the outset, the most natural approach felt like assigning each task an estimated duration, and reflecting on story points as hours.  This allowed me to capacity plan the first couple of sprints/ iterations based on the time I had available..... I await to see if I will continue this as the project progresses, or whether I move to a more fluid interpretation of SPs.
* However with the magic law of time (better check what magic law this is) creative tasks in which I am fully engaged make the time fly, meaning I can spend quite a bit of elapsed time but without feeling the straing, whereas less desirable tasks cause time to drag!  <- how does this reflect story points?
* Agile representation using github tools

   
### Project
A github project was created within the Financial_Planner repo.  At a high level the project details are very simple really just a name and description.
<details><summary>GitHub Project Setup</summary>
<img src="./django_financial_planner/docs/readme_images/agile-overview-of-project2.png">
</details>


### Issue Template
<details><summary>Issue template - User Story</summary>
<img src="./django_financial_planner/docs/readme_images/agile-issues-template.png">
</details>
    
At the outset, an issue template was created specifically for user stories.  This holds 5 sections:  
* EPIC:  The parent functional theme for this user story
* A statement of what is to be achieved in the format 'As a **role** I want to **action** to achieve **goal**'.
* Assumptions made when creating this isssue (e.g. pre-requisites)
* Acceptance Criteria: List of conditions to demonstrate the issue has been satisfied/resolved
* Tasks:  Checkbox-marked list of tasks to address this user story.

Mid-way through the project, I created a template to capture project bugs to facilitate separate tracking/reporting.


### Project Issues
Issues were created to track planned end-to-end work in Financial_Planner, using the issue template for consistent appearance and content.   
Financial_Planner project scope includes UX design tasks, agile project setup, development tasks, documentation,  and testing.
<details><summary>Example issue - user story</summary>
<img src="./django_financial_planner/docs/readme_images/agile-issue-example-user-story.png">
</details>

Some of the issues created were in fact tasks, which underpinned several user stories:
<details><summary>Example issue - task</summary>
<img src="./django_financial_planner/docs/readme_images/agile-issue-example-task.png">
</details>


### EPICs
An epic in agile is a large body of work that can be broken down into a number of smaller stories, which are represented as github Issues.
The Financial_Planner project uses custom fields to hold the epic name, some initial high-level epics:  Agile, UX, Docs, MVP.
For clarity EPIC is also listed at the top of each issue.
<details><summary>EPICs</summary>
<img src="./django_financial_planner/docs/readme_images/agile-epics.png">
</details>


### MoSCoW prioritisation
For prioritising user stories and known tasks, I assigned a label to each issue, one of:
* Must-have
* Should-have
* Could-have (or nice-to-have)
* Won't have (perhaps its a never, or perhaps this just means 'not at this release')
To make selection easier (ensure that these appeared at top of label list in the order above) I preceded each label with a number as shown:
<details><summary>MoSCow labels</summary>
<img src="./django_financial_planner/docs/readme_images/agile-issues-moscow-prioritization.png">
</details>


### Story Points
Story points are intended as a 'level of required effort' measure.  I used a custom issue category field to represent these. 
While at the beginning it was easiest to think of story points in terms of 'hours', as the sprints passed it became easier to assess relative to work already completed.
An observation would be that interpreting story points as 'hours' is somewhat one-dimensional, as sometimes the elapsed hours can be greater or lesser depending on mood, state of flow etc.


### Milestones
While this is a relatively short project (developed over 2 months duration), there was sufficient opportunity to set milestones for MVP (mostly consisting of must-have issues) and releases.
The use of MVP milestone encouraged a 'deploy-early' mindset whereby the software could be delivered incrementally, with successive releases building on proven, working software.  
When creating the milestone a due date is needed, initially I set a due date of 3 weeks prior to deadline for MVP, with additional release dates scheduled up to the project deadline.

This approach ensured, it would be possible to deliver a working, functional system, even if difficulties were encountered with implementing some of the 'could-have' features..
<details><summary>Milestones</summary>
<img src="./django_financial_planner/docs/readme_images/agile-milestones.png">
</details>

### Sprints and Iterations
In Agile methodology, effort is timeboxed into Srints, with a kickoff at the start of each Sprint time period, in which items from the product backlog are made ready for work (groomed) by ensuring all the details are completed on the user-story/issue card (task details, acceptance criteria, priority, dependencies, Story Point estimate ) before a developer starts working on it.  At the end of a sprint a retrospective should be undertaken to determine what worked well or not during that sprint.
For Financial_Planner a time-period of weekly sprints was chosen.  Loosely (given that the developer consisted of a one-person team), the sprint ran from Monday-Sunday inclusive, and the aim was to complete certain agreed user stories during a particular sprint.

<details><summary>Sprints/ github Iterations</summary>
<img src="./django_financial_planner/docs/readme_images/agile-sprint-iteration-weekly.png">
</details>

Initially when performing the design tasks (effectively the first four sprints), the timeboxing aspects were not fully respected.
However from sprint5 onwards (the first programming sprint), it became easier to decide clearly what was to be included at the outset of each sprint, and to pull specific issues from the backlog and ensure that they were progressed during the planned sprint. 


### Issue Lifeycle
An issue is set to progress through a number of stages, each represented by a status during its lifecycle.  A issue can be closed or deleted at any time, however best practise is to progress through:
* Backlog 
* To-do
* In-progress
* Review
* Done
(Can possibly add a flowchart here for visibility of lifecycle)
(Might be worth discssing status of Wont_have here also).


### Tabular Projects View
The tabular view of projects was very useful at the backlog grooming stage, as it shows open issues, and gives easy visiblity of associated fields, e.g. story points, epic, assigned sprint, etc 
<details><summary>Projects - Tabular view</summary>
<img src="./django_financial_planner/docs/readme_images/agile-overview-of-project.png">
</details>

<details><summary>Projects - Tabular view2</summary>
<img src="./django_financial_planner/docs/readme_images/agile-issues-tabular-view.png">
</details>

    
### Kanban board
Within a sprint, the kanban board provides invaluable visual tracking.  
In the Financial_Planner kanban board, issues progress from leftmost column (backlog) to rightmost (done)
Note that each column holds a descriptor to tell you what is happening to issues within the column.
<details><summary>Projects - Kanban (simple)</summary>
<img src="./django_financial_planner/docs/readme_images/agile-issues-kanban-view.png">
</details>

An improved kanban view (developed mid-way through the project) is shown here, note that this shows:
* the number of issues at each kanban board state (e.g. highlighted in blue for InProgress column)
* The storypoints for each individual issue, as well as the total storypoints at each lifecycle status (e.g. highlighted in green for 'Todo' column)
* The EPIC associated with each issue (e.g. highlighted in pink within the 'Done' column)

![Projects - Rich Kanban board](./django_financial_planner/docs/readme_images/agile-issues-kanban-view-sp-epic-num-issues-per-col.png?raw=true "Improved kanban board with lots of information")

 
### Agile Observations and learnings
* Observation from hackathon - short user story names are best for visibility and tracking
* Observation from hackathon - a user story is generally a fairly big block with a number of subtasks.  It is not advisable to have an entire user story which is longer than a sprint, as it will be carried forward in the 'to do' or 'in progress' bucket without clear visibility.  Therefore likely to try breaking a complex user story into subtasks.  Both the user story and the sub tasks will be listed as issues, the user story will remain in the 'to do' bucket after grooming, and its tasks will be ticked off when their individual issues are completed.  The individual issues will move through the kanban board lifecycle of backlog -> to do -> in progress -> review -> done.  The 'parent' user story will remain at 'to do' (or possibly 'in progress'???)
* Observation from hackathon - when merging of PR (pull requests) was performed in a distributed development environment, it was possible to link the PR to a kanban issue, and to automatically update the issue status based on the PR.   I would be interested in exploring how ths might be done for a solo developr (possibly workflows?)
* Observation - if I reference the issue # on a commit (but must be in the format #8 ) then I can hyperlink from that commit message back to the relevant user story or issue.
* Use of EPIC as a label rather than as an issue - this was an early decisiion, although when reviewing our cohort leader Alan B's PP4 project, he showed how he had used Issues within Github to represent EPICS.  This seemed to work really well as it was possible to demonstrate a hierarchy of EPIC -> issues by including a link to the sub-issues within the EPIC 'issue' body.  Thus it was possible to click on the issues within the EPIC, check their status, then return to the EPIC.
At the time of seeing this I had already committed to using labels to represent EPICs, so I stayed with my original approach just to see how it would work in practice.
* Use of a public project repo - I made the repo public early on, as I had assumed this was needed for assessment.  And about half way through I was surprised to see some comments on my tasks from another (unknown) github user offering assistance with development - kind of like an open source approach.  So they had commented on a couple of tasks.  I kept the repo public, but changed the settings so that only users who had previously committed to the repo could comment, and I blocked that particular user from the workspace....


## Features 
 
### F01 
<details><summary>Introduction screen</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/django_financial_planner/docs/readme_images/f01_intro.jpg"></details>
<br>
On first using the game an introduction window is shown, the user can choose 'Play' or 'How to Play' buttons.  The intro page shows the current date, the Financial Planner day number, and some copyright and acknowledgement notices.
This addresses user stories SO_01, SO_02, FTU_01, FTU_02, FTU_03
<br>
<br>

### F02 'How To Play' Screen
<details><summary>How To Play screen</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/django_financial_planner/docs/readme_images/f02_help.jpg"></details>
<br>
A modal 'How to Play' explains how to play and some of the subtleties of the calculations.  Available from the 'how to play' button on the Intro screen, or from the navbar help icon on all screens.   The 'How to Play' window can be scrolled to see full text, and is closed by clicking on the X in top right hand corner, at which point it disappears from screen.
<br>
<br>      

### F03 Play button
The Play button ![Play button](./django_financial_planner/docs/readme_images/f03_play_button.jpg?raw=true "Image of Play button") allows the user to go directly to a game screen, and immediately play a game ('call to action').
<br>
<br>

### F04 Randomly selected solution
<details><summary>Array of potential solutions</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/django_financial_planner/docs/readme_images/f04_solution_array.jpg"></details>
(Dont look too closely or you will ruin the surprise of playing the game!)<br>
An array of solutions is maintained, and, when the game starts, an entry is randomly chosen from this array.  At the time of development this array contained approx 20 entries, which is sufficient for demo purposes, it is envisioned that this will be extended in the future.
<br>
<br>

### F05 Uncluttered game screen
<details><summary>Initialised game screen</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/f05_uncluttered_game_screen.jpg"></details>
The game screen is presented to the user fully initialised (ie a target value has been set and populated to each grid row).  The screen is free of ads and supplemental displays, which allows the user to focus on the game.
<br>
<br>

### F06 Consistent Navbar<br>
The Navbar is consistent throughout the website, 404 and feedback pages.  (modals/pop-ups are used to show intro and help pages, which don't show the navbar but when they are closed, the navbar can be seen on the underlying page)  Contains icons for Help, Stats and Settings.
![Navbar](./docs/readme_images/f06_navbar.jpg?raw=true "Navbar image")
<br>
<br>

### F07 Game grid
<details><summary>Game panel</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/f07_game_grid_in_progress.jpg"></details>
Interactive and responsive game panel which allows the user to record one set of guess tiles per attempt (the current attempt # is shown at top of screen).  The game grid is initially blank, and will be populated with successive user guesses.
Interactivity/feedback:  when the user presses ENTER to submit a guess, the guessed tiles update as green(correct); orange(present) or grey(absent).
<br>
<br>

### F08 Keyboard display
<details><summary>Keyboard</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/f08_keyboard_grid.jpg"></details>
A pseudo-keyboard shows the permitted entries.  The user must click on the keys using a mouse pointer to select an entry.  When a keyboard key is pressed, its colour flickers to light blue, and the key value is loaded to the current guess row on the game grid.  So the keyboard is the main user control for the game, and each press of a keyboard key triggers an action.   (keys 1-20, */-+ populate the game grid).<br>
When the user presses ENTER to submit a guess, the keyboard elements used within the guess also update as green(correct); orange(present) or grey(absent).
<br>
<br>

### F09 DEL key
A backspace key is provided which allows the user to remove the last keyed entry on the current grid row.
<br>
<br>

### F10 ENTER key
The ENTER key submits the current guess row for validation. 
<br>
<br>

### F11 Equation validation
When a guess is submitted, the equation which the user has submitted is parsed and validated as follows - the entries at the second and fourth columns are assessed to ensure these contain an operator (plus minus multiply divide); the guessed equation is then validated to check if it equates to the target value.  If not, an error message is shown, however the game (at this version) will still progress to individual element valuation.
![If equation has wrong total](./assets/readme_images/f11_wrong_total.jpg?raw=true "Equation calculates to incorrect total")
<br>
<br>

### F12  Individual guess element validation
<details><summary>Feedback on keyboard re guessed solution</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/f12_keyboard_interaction_feeback.jpg"></details>
Each element of the guess is compared to the solution, and its tile colour amended according to whether the guessed tile is:
* correct (green)- tile value is at this position in the solution;
* present (orange)- tile value is at a different position in the solution;
* absent (grey) - tile value is not in the solution.
![Feedback on game panel re guessed solution](./docs/readme_images/f12_game_interaction_feeback.jpg?raw=true "Image of guessed tiles changing colour")

The corresponding keyboard grid value is coloured on the lower part of the screen, e.g. '5' guessed correct; will colour both the row tile and the keyboard key green.  A (hidden) count of the number of correct elements is maintained.
<br>
<br>

### F13 Success message
<details><summary>Appropriate success message, content varies by # of attempts</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/f13_attempt4_result.jpg"></details>
 This displays when all elements correctly guessed.  A pop-up message with the appropriate text appears.  This text mimics the Wordle site, so depending on the  number of attempts the successful user can get (Genius, Magnificent, Impressive, Splendid, Great, Phew).
<br>
<br>

### F14 Solution display if exceeded 6 attempts
<details><summary>Solution display if 6 unsuccessful guesses</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/f14_exceeded_6attempts.jpg"></details>
A pop-up message with the appropriate text appears if the user has matched the entire solution equation.  This text mimics the Wordle site, so depending on the  number of attempts the user can get (Genius, Magnificent, Impressive, Splendid, Great, Phew)
<br>
<br>

### F15 User Statistics 
<details><summary>User statistics</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/f15_user_statistics.jpg"></details>

This screen is really a placeholder for future functionality as would like to display some of the statistics for a player over a number of games<br>
<br>

### F16 Settings and Feedback
<details><summary>User settings</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/f16_settings_feedback.jpg"></details>

This allows the user to provide feedback and to choose to join a daily reminder mailing list.  There are placeholder questions here for future Limit to one game daily (preset to 'no limit');
Difficulty levels: easy or difficult (preset to 'difficult').
Share image of solution to clipboard (future)
<br>
<br>

### F17 Responsiveness
The site is designed to be fully responsive so it can be played on a range of convenient devices.

### Features in Scope 

<details><summary>Mapping of user stories to features</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/user_stories_vs_features.jpg"></details>

This website includes 3 pages and 16 features 
The pages - which effectively bring the features lited in the previous section together - are:
* Landing Page (see feature F01 Intro Screen)
* Settings page (see feature F16 Feedback and settings )
* 404 error page 

- __404 Error Page__ 
This allows graceful failure, where the header and footer are preserved, allowing the user to navigate away from an error page using the site navigation (rather than the back button).

<details><summary>404 error page</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/p03_error_404_page.jpg"></details>

### Implementation Decisions
Pre-defined calculations are stored in a multi-dimensional array as follows:
Solution [
[ 3, *,_ 7 * 2, 41_], // ie 3 * 7 * 2 = 41
[2, + , 5 * 7, 41] //ie 2 + 5 * 7 = (7) * 7 = 41
]
Each day's equation can therefore be referenced as Solution[day#]
Each days' elements can be referenced as solution[day#, element#]
This is useful when comparing a user entry for a match.

Daily user entries are stored in an array of 7 x 6 rows as follows:
Attempt [(undef, green, orange), (undef/green/orange), (undef/green/orange), (underf/green/orange), (undef/green/orange), (success)]
Attempt attempt#, element# can be compared to each of the entries in solution [day#, element#y] to search for a match - if found then if attempt.element# matches solution.element# then green, else orange.

Break out of loop when success, or when 6 tries reached.
<br>

### Features Left to Implement
While Financial Planner, at the current version, provides the 'engine' for pattern matching and calculation, there are a number of desirable features which exist in the current version of Wordle and which would greatly add to the user experience for Numble.

Choose difficulty level
* Allow the user to choose difficulty level EASY (all numbers <= 10) or DIFFICULT (numbers <=20 included).  Note that this has been allowed for in the array of solutions, these are classified according to difficulty, so this may be an 'easy win' future feature.

Allow the user to limit to one game daily
* One of the beautiful features of wordle is its limited-release mode whereby only one puzzle is released daily ... this creates a sense of anticipation and the user wants more, they don't get the chance to become bored or tired with the game.  
* Financial Planner at the current version, allows the user to play continuously by refreshing the browser.  This is useful when in testing and demonstration mode, but ideally the default would be one game per day.

Preserve user statistics from one game to the next
* This has been allowed for within the user interface by providing a statistics page, however the stats currently only relate to the latest game played.   Tracking of # of days 'winning streak' is very motivating to the user.

Share results
* Wordle has a feature whereby a user can share their pattern matching results without revealing the underlying solution.
<br>
<br>
               
## Technologies

### Langugages
- HTML 
- CSS
- Javascript

### Frameworks & Tools
* Github:  used to maintain the code repository, and for some readme edits and commits
* Git
* Gitpod:  used for editing and for tracking code commits back to Github
* Balsamiq:  used for wireframing
* Google Fonts: used to locate suitable fonts for website


## Validation 

### HTML Validation 
- HTML
  - No errors returned on the index html pages when checked in the W3C validator:
  - [W3C validator - index page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdeemccart.github.io%2FCI_PP4_Financial_Planner%2Findex.html) 
  - [W3C validator - 404 page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdeemccart.github.io%2FCI_PP4_Financial_Planner%2F404.html)
  
  - [W3C validator - settings page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdeemccart.github.io%2FCI_PP4_Financial_Planner%2Fsettings.html)

### CSS Validation
  - No errors returned when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https://deemccart.github.io/CI_PP4_Financial_Planner/&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) 

### Javascript Validation
  - No errors returned, when javascript was pasted into the jshint validator - however 10 unused variables were identified, which are the function names.    
<details><summary>jshint - no errors however the function names were identified as unused variables</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/jshint_result.jpg">
</details>

### Accessibility
The site was tested using the WAVE WebAIM accessibility evaluation tool.
All pages pass with 0 errors 
- [Accessibility: index page](https://wave.webaim.org/report#/https://deemccart.github.io/CI_PP4_Financial_Planner/)
- [Accessibility: 404 page](https://wave.webaim.org/report#/https://deemccart.github.io/CI_PP4_Financial_Planner/404.html)


### Performance
Performance for all pages was tested using the Lighthouse tool within Google Chrome.  Performance was at 98% for the index page (intro modal).

<details><summary>Performance: Index page</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/performance_lighthouse_intro_page_230602.jpg">
</details>


### Device Testing
The website was tested on the following devices:
* HP laptop
* Samsung Galaxy S10 tablet
* Motorola G(7) android phone

### Multi-browser Testing
The website was tested on the following browsers:
* Google Chrome v112.0.5615.138 (HP laptop)
* Google Chrome v112.0.5615.136 (Samsung Galaxy tablet)
* Mozilla Firefox v112.1.0 (Motorola g(7) phone)

### Testing User Stories
![User story testing](./assets/readme_images/user-stories-checked-against-features.jpg?raw=true "testing user stories")

### Bugs and issues
<details><summary>issue tracker</summary>
<img src="https://deemccart.github.io/CI_PP4_Financial_Planner/docs/readme_images/issue_tracker.jpg">
</details>
Quite a few calculation and display issues were encountered during development, the above lists the issues encountered and resolved.

## Deployment
<br>
* The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab - pages 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://deemccart.github.io/CI_PP4_Financial_Planner/index.html

* To fork the repository:
- Go to the GitHub repository
- Click on Fork button in the upper right hand corner

* To clone the repository:
- Go to the GitHub repository
- Locate the Coe button above the list of files and click it
- Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to you clipboard
- Open Git Bash
- Change the current working directory to the one where you want the cloned directory
- Type git clone and paste the URL from the clipboard($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
- Press Enter to create your local clone


## Credits 
Multiple sources were used in assembling this site.


### Content - Financial Planner
* Inspiration taken from many many sources
* Existing sites and offerings towards financial literacy in Ireland:  (list below)
* 
### Financial Planner site ethos - authenticity
https://nobsmarketplace.com/blog/how-do-you-know-if-website-authoritative/ offers a definition of an authoritative website as 'a trusted source that offers reliable information to users'
https://nobsmarketplace.com/blog/how-do-you-know-if-website-authoritative/ factors to determine an authoritative website: site domain name/url; value offered to the user; reputable sources (with verifiable credentials); quality of inbound & outbound links; website UX, design & functionality; proven user trust & engagement (e.g. measured by organic comments, likes and shares given by customers/users, as well as the quality of the audience the website has attracted)

### Agile implementation in github
* https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-text-and-number-fields#adding-a-number-field to understand how story points might be represented in GitHub
 
### Code - Financial Planner
* https://laracasts.com/series/wordle-workshop/episodes/2 for tips on building a wordle-like grid (using HTML or JS)
* https://www.youtube.com/watch?v=j7OhcuZQ-q8 Build a Wordle clone using HTML, CSS & Javascript! : used for tips on keyboard panel building (but thereafter preferred to code independently as found that coding shortcuts proposed were not always comprehensible to a new JS developer!)

### References
The following sites were ued for research and better understanding while creating this website: 

 
### Acknowledgements
* I would like to sincerely thank my mentor, Mo Shami for his enthusiasm and support throughout.
* I would also like to thank Derek and my family for their personal support.


