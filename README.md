# BST236 OnetCompare App

This app is designed to compare occupations using data from the O*NET database. The app is built using Dash and Plotly with user-friendly interfaces to facilitate data interaction.

To see the current online version of the app hosted on Heroku, visit: [bst236-onetcompare-currentcommit](https://bst236-onetcompare-a23cabb5a2d4.herokuapp.com/). The online app uses Python version 3.10. 

To download, modify, and host this app locally, clone this repo, enter into the directory, and install all necessary packages above base Python:

```bash
git clone https://github.com/panevins/bst236-onetcompare-app.git
cd bst236-onetcompare-app
pip install -r requirements.txt
```

All files used in the production of the interactive visualization app are available in the main directory. 

* To update the occupations list, change components of `download_occups` in `vis_download_files.py`

* To update the datasets being used, first make sure their elements are available in `element_name_dict.json`. Then, update `layout.py` and `app.py`, copying the format for Skills, Abilities, and Knowledge (update: `dcc.Checklist` div, add another child to `html.Div(id='element-dropdowns-container')` for a dropdown, add a line to `update_dropdown_visibility`, the callbacks, and the `update_radar_plots`'s `filtered_df`). (Note: these three datasets are all on a scale of 0-7, other datasets may not be. Consider scaling for more interpretable visualization.)

## License

O*NET Content License
----------------------
This project incorporates information from O\*NET Web Services by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA). O\*NET® is a trademark of USDOL/ETA. Use of O\*NET data is subject to the O\*NET Content License, which can be found at:
https://www.onetcenter.org/tcc.html

MIT License
-----------
Copyright (c) 2025 P Nevins

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.