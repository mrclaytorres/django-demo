# Django Demo

A Django demo using Metronic template

## Requirements
Assuming you already setup Django and your Python environment.

## Build Assets

1. Start a command prompt window or terminal and change directory to starterkit/_keenthemes/tools

  `$ cd starterkit/_keenthemes/tools`  

2. Install dependencies with either one, yarn or npm:

  `$ yarn install`  

  You can use either one.

  `$ npm install`

3. You can use Gulp  or Webpack  commands to bundle theme assets. The below command will compile all the assets(sass, js, media) to starterkit/assets folder:

  For gulp use command:  
  `$ gulp`  

  For webpack use command:  
  `$ npm run build`

## Run Django

1. Navigate your prompt to starterkit folder.

	`$ cd starterkit`

2. `python manage.py runserver`

3. When the above runserver command is running, the warning below may appear. Run the below command to fix it. Below is an optional command to apply SQLite migration.

	`$ python manage.py migrate`
    
    
## Adding Demo data

On the `/demo` you'll find a `demo.csv` that contains dummy data that you can import and use. I've created a script to import that data into the database.

Note: Make sure that you did `makemigrations` and/or `migrate` commands so that the demo model will be created in the database.

Use this command in the project root folder:  

`$ python manage.py runscript load_data`