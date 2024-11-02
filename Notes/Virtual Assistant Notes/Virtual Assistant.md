****
**Project Overview**
- Project Name: Virtual Assistant version 1.0
- Date: "N/A"
- Author: Nicholas Waugh
- Description: currently I have a really bad issue with connecting with others and have a poor communicative skills. For this Project I want to create a virtual assistant. An AI buddy that acts as a teammate that helps motivate the user such as tallying the accomplishments the user makes, check the calendar, and allows the AI to assist in your journey I.E. help writing and reading document.

**Requirements**
- **[[Task Management System (CRUD)]]**
	- Description: Allow the program to manage the tasks.
	- Inputs: Text
	- Output: Task Status message
	- Dependencies: User
	- Status: Not Started
- **[[Schedule Management System (CRUD)]]**
	- Description: Authorize the program to set a schedule
	- Inputs: Text
	- Output: Schedule Status
	- Dependencies: User and Task Management System
	- Status: Not Started
- **[[Notification System]]**
	- Description: Send Reminders to upcoming deadline tasks from the Task management system
	- Input: Task Due Dates
	- Output: Desktop Notification
	- Dependencies: Schedule Management System
	- Status: Not Started
- **[[User Registration (CRUD)]]**
	- Description: Allows the User to create an account for recognition
	- Input: Email, Password
	- Output: Success/Error Message
	- Dependencies: N/A
	- Status: Not Started
- **Level Up System**
	- Description: Gives the user a progress system for the user's improvements
	- Input: Task Management System
	- Output: Congratulate message or failure message
	- Dependencies: Task Management System
	- Status: Not Started
	
**Architecture and Design**
	[[The following is highlighted in Graph View]]
**Development Environment**

Visual Studio Code Python 3.12, Windows 11 Home 24 H2 HP Laptop 15-dy2xxx 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz  2.40 GHz

**Database Design**
	==**Tasks DB**==
		- Task_ID SERIAL PK
		- Title VarChar(255) NOT NULL
		- Category VARCHAR(50)
		- Description TEXT
		- Status VARCHAR(20) Default 'Pending'
		- Assigned_to INT
		- Due_date VARCHAR(50)
		- Created_at --"TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
		- Updated_at --"TIMESTAMP DEFAULT CURRENT_TIMESTAMP IN UPDATE CURRENT_TIMESTAMP"
		- Priority VARCHAR(20) (Varies to continually, low, medium, high)
		- Reminder_Time TIMESTAMP
		- Reminder_Interval INTERVAL
	==**Users DB**==
		- User_ID SERIAL PK
		- email VARCHAR(255) NOT NULL
		- name VARCHAR (50)
		- created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
		- last_login TIMESTAMP
		- currentlevel INT DEFAULT 1
		- XP INT DEFAULT 0,
		- phone_number VARCHAR(20)
		- role VARCHAR(20)

**API Documentation**

**Testing**

**Deployment**

**Maintenance and Troubleshooting**