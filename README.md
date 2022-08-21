<p align="center">
<a href="https://dscvit.com">
	<img width="400" src="https://user-images.githubusercontent.com/56252312/159312411-58410727-3933-4224-b43e-4e9b627838a3.png#gh-light-mode-only" alt="GDSC VIT"/>
</a>
	<h2 align="center"> Meeting MOM BOT (NLP/ML) </h2>
	<h4 align="center"> Converts a meeting transcript to its minutes of meeting <h4>
</p>

---
[![Join Us](https://img.shields.io/badge/Join%20Us-Developer%20Student%20Clubs-red)](https://dsc.community.dev/vellore-institute-of-technology/)
[![Discord Chat](https://img.shields.io/discord/760928671698649098.svg)](https://discord.gg/498KVdSKWR)

## Features
- [x]  Summarizes a meeting into its minutes of meeting
- [x]  A FastAPI endpoint to get the MOM

<br>

## Notebook & Model
- Notebook: https://www.kaggle.com/code/iamyajat/meeting-transcript-summarization
- Model: https://www.kaggle.com/code/iamyajat/meeting-transcript-summarization/data

## Dependencies
 - Python 3.8
 - Pytorch
 - FastAPI


## Running

1. Clone the repository
   ```sh
   git clone https://github.com/GDGVIT/mom-bot-ml.git
   ```
2. Install `virtualenv`
   ```sh
   pip install virtualenv
   ```
3. Create a virtual environment
   ```sh
   python -m venv env
   ```
   ```sh
   .\env\Scripts\activate
   ```
4. Install all requirements
   ```sh
   pip install -r requirements.txt
   ```
5. Place the model files in the following path:
   ```sh
   ./assets/t5-epoch-x-train-loss-xxx-val-loss-xxx
   ```
5. Start the API
   ```sh
   uvicorn main:app --reload
   ```
   
## Contributors

<table>
	<tr align="center">
		<td>
		Yajat Malhotra
		<p align="center">
			<img src = "https://avatars.githubusercontent.com/u/68477362?s=460&u=3512e6223472e97a050f292478d125602c371fec&v=4" width="150" height="150" alt="Yajat Malhotra">
		</p>
			<p align="center">
				<a href = "https://github.com/iamyajat">
					<img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="GitHub"/>
				</a>
				<a href = "https://www.linkedin.com/in/iamyajat">
					<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36" alt="LinkedIn"/>
				</a>
				<a href = "https://www.twitter.com/iamyajat">
					<img src = "https://www.iconninja.com/files/51/256/860/twitter-media-social-network-circle-icon.svg" width="36" height="36" alt="Twitter"/>
				</a>
			</p>
		</td>
	</tr>
</table>

<p align="center">
	Made with ❤ by <a href="https://dscvit.com">GDSC VIT</a>
</p>
