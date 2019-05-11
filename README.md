# cxxxxr
Application used to pull CRE contacts into a CSV file
### Step 1 - Search in CRE program
- Perform a search for the contacts that are deal makers.
### Step 2 - Extract pages
- Open each result page and save as an .html file; use separate file names so they don't overwrite.
- Copy the 'ResultContactCpd' files (.html) out of the folder and rename them anything; keep .html extensions.
### Step 3 - Relocate the .html files
- Copy the files into the 'html_files' folder.
### Step 4 - Run progam
- Run the cxxxxr.py program.
- User input is required for the 'Email list name'.  
- The list name is so can be determined which list you want it in for Constant Contact or another email marketing app.
- Final output is in a file called 'export.csv'.
