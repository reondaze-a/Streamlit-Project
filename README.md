# TripleTen-SDA-Project
Software Development Tools Project: Pokemon Stats Graph

Hello! This web app was built to see the correlation between Pokemon stats up to Generation 6, based on the types.
Based on your selected input, the app will graph either a Scatterplot or a Histogram to show the Data. The input consists of the 
type of Pokemon and the stat on which you would like the graph to show. There's also an individual Pokemon Stat Calculator located on app2.py

The libraries I've used include:
* Streamlit
* Plotly Express
* Numpy
* Pandas

And I also used a self-made module: pkmn_func.py

To launch it on your local machine, pull the repository to your local machine and then use a command shell(CMD, Git Bash, PowerShell)
and direct yourself to the repository's directory.  Go to `.streamlit` directory and disable or delete the `config.toml` file. Then in the command shell, enter the command: `streamlit run app.py` or `streamlit run app2.py`.

**Must have streamlit installed on your machine!**
If you don't you can run the command `pip install streamlit`.

URL to web-app : https://tripleten-sda-project.onrender.com/
