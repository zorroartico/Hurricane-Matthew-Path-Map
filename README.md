# Hurricane-Matthew-Path-Map
[Project] Hurricane Matthew path map in Python

<h3>Preface</h3>
This was a personal project I did at leisure. Rather than using ArcMap (ArcGIS) to map things for me, I wanted to create a map entirely based on Python code from scratch. This project was meaningful in a way that it taught me how to map things only in programming language.

<h3>Note about Data Organization</h3>
<ol>
<li>Obtain IBTrACS Dataset from NOAA (you can download it in .csv file). That dataset contains information of tropical cyclones in Atlantic Ocean from early 1900s to 2016.</li>
<li>Open the dataset in Excel. Perform data cleaning (i.e. specify one hurricane you want to focus on).</li>
<li>Eliminate identifiers that seem unnecessary. (note: The number '999' on numerical identifiers mean that they are not recorded.)</li>
</ol>

<h3>Note about the map</h3
<ul>
<li>Matplotlib was used to map the track of hurricane matthew. Instructions for mapping using basemap are found <a href='https://matplotlib.org/basemap/users/examples.html'>here</a>.</li>
<li>I used Python 3.6.3.</li>
<li>I added some comments on the .py files for brief explanation.</li>
<li>I like to refactor codes because I don't want main.py file to be increasing in length.</li>
</ul>
