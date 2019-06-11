

```python
import pandas as pd
import numpy as np
```


```python
df = pd.read_csv("deliveries.csv")

```

<h3>Which bowler has hit for maximum number of 1s</h3>


```python
df2 = df.query(" total_runs == '1' ")
df2.groupby('bowler')[['total_runs']].count().sort_values('total_runs',ascending=False).head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_runs</th>
    </tr>
    <tr>
      <th>bowler</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Harbhajan Singh</th>
      <td>1549</td>
    </tr>
    <tr>
      <th>R Ashwin</th>
      <td>1415</td>
    </tr>
    <tr>
      <th>A Mishra</th>
      <td>1414</td>
    </tr>
    <tr>
      <th>PP Chawla</th>
      <td>1311</td>
    </tr>
    <tr>
      <th>DJ Bravo</th>
      <td>1189</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Which batsman got stumped out maximum number of times?</h3>


```python
df.query("dismissal_kind=='stumped'")[['player_dismissed','dismissal_kind']].groupby('player_dismissed').count().sort_values('dismissal_kind',ascending = False).head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dismissal_kind</th>
    </tr>
    <tr>
      <th>player_dismissed</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>SK Raina</th>
      <td>8</td>
    </tr>
    <tr>
      <th>RV Uthappa</th>
      <td>7</td>
    </tr>
    <tr>
      <th>AT Rayudu</th>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.read_csv("matches.csv")
```

<h3>Which team has won maximum number of matches while chasing?</h3>


```python

df3= df2.query(("toss_decision=='field' and toss_winner == winner or toss_decision=='bat' and toss_winner != winner"))[['id','winner']].groupby('winner').count().reset_index().sort_values('id',ascending=False).head(5)
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>winner</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>Kolkata Knight Riders</td>
      <td>58</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Mumbai Indians</td>
      <td>51</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Chennai Super Kings</td>
      <td>49</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Royal Challengers Bangalore</td>
      <td>49</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rajasthan Royals</td>
      <td>46</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Which team has lost maximum number of matches while chasing?</h3>


```python
df4 = df2.query(("toss_decision=='field' & (toss_winner != winner )or toss_decision=='bat' & (toss_winner == winner)"))[['id','winner']].groupby('winner').count().reset_index().sort_values('id',ascending=False).head(5)
df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>winner</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>Mumbai Indians</td>
      <td>58</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Chennai Super Kings</td>
      <td>51</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kings XI Punjab</td>
      <td>38</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Royal Challengers Bangalore</td>
      <td>35</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kolkata Knight Riders</td>
      <td>34</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Which toss decision is best for each ground?</h3>


```python
df_field_win = df2[df2['toss_winner']==df2['winner']].query("toss_decision=='field'")[['winner','venue']].groupby('venue').count()
df_bat_win = df2[df2['toss_winner']==df2['winner']].query("toss_decision=='bat'")[['winner','venue']].groupby('venue').count()
df_bat_win
df_field_win.merge(df_bat_win,on='venue',suffixes=('_field','_bat')).head(3)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>winner_field</th>
      <th>winner_bat</th>
    </tr>
    <tr>
      <th>venue</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Barabati Stadium</th>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Brabourne Stadium</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>De Beers Diamond Oval</th>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Which player has won maximum number of MoM awards while chasing?</h3>


```python
df2 = df2[df2['win_by_wickets']>0][['player_of_match','win_by_wickets']]
playerdm= df2.groupby('player_of_match').count()
playerdm[playerdm.win_by_wickets==playerdm.win_by_wickets.max()]

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>win_by_wickets</th>
    </tr>
    <tr>
      <th>player_of_match</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>YK Pathan</th>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Which batsman has played maximum number of dot balls?</h3>


```python
dot_balls_df = df.query('total_runs==0')[['batsman','total_runs']]
new_df = dot_balls_df.groupby('batsman').count()
new_df[new_df.total_runs == new_df.total_runs.max()]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_runs</th>
    </tr>
    <tr>
      <th>batsman</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>V Kohli</th>
      <td>1369</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Which non-striker has been part of maximum number of runouts?</h3>


```python
df_new = df.query('dismissal_kind == "run out"')[['dismissal_kind','non_striker']]
df4 = df_new.groupby('non_striker').count()
df4[df4.dismissal_kind == df4.dismissal_kind.max()]

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dismissal_kind</th>
    </tr>
    <tr>
      <th>non_striker</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>KD Karthik</th>
      <td>16</td>
    </tr>
    <tr>
      <th>SK Raina</th>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>



<h3>The number of venues in each season</h3>


```python
matches = pd.read_csv("matches.csv")
matches[['season','venue']].groupby('season').count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>venue</th>
    </tr>
    <tr>
      <th>season</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2008</th>
      <td>58</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>57</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>60</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>73</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>74</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>76</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>60</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>59</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>60</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>59</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>60</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>



<h3>How many matches played by each team and how many won</h3>


```python
new_df = pd.concat([matches['team1'],matches['team2']]).value_counts().reset_index()
new_df.columns=['index','matches_played']
match_won = matches['winner'].value_counts().reset_index()
new_df.merge(match_won,on='index')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>matches_played</th>
      <th>winner</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mumbai Indians</td>
      <td>187</td>
      <td>109</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Royal Challengers Bangalore</td>
      <td>180</td>
      <td>84</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kolkata Knight Riders</td>
      <td>178</td>
      <td>92</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kings XI Punjab</td>
      <td>176</td>
      <td>82</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Chennai Super Kings</td>
      <td>164</td>
      <td>100</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Delhi Daredevils</td>
      <td>161</td>
      <td>67</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Rajasthan Royals</td>
      <td>147</td>
      <td>75</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Sunrisers Hyderabad</td>
      <td>108</td>
      <td>58</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Deccan Chargers</td>
      <td>75</td>
      <td>29</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pune Warriors</td>
      <td>46</td>
      <td>12</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Gujarat Lions</td>
      <td>30</td>
      <td>13</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rising Pune Supergiant</td>
      <td>16</td>
      <td>10</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Delhi Capitals</td>
      <td>16</td>
      <td>10</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Kochi Tuskers Kerala</td>
      <td>14</td>
      <td>6</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Rising Pune Supergiants</td>
      <td>14</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Which venue was the most used throughout the history of IPL</h3>


```python
df2['venue'].value_counts().reset_index().head(5)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>venue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Eden Gardens</td>
      <td>77</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Wankhede Stadium</td>
      <td>73</td>
    </tr>
    <tr>
      <th>2</th>
      <td>M Chinnaswamy Stadium</td>
      <td>73</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Feroz Shah Kotla</td>
      <td>67</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rajiv Gandhi International Stadium, Uppal</td>
      <td>56</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Most favorite umpire</h3>


```python
df_umpires = pd.concat([df2['umpire1'],df2['umpire2']])
df_umpires =  df_umpires.value_counts().reset_index()
df_umpires.columns = ['umpire','matches']
df_umpires.head(3)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>umpire</th>
      <th>matches</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>S Ravi</td>
      <td>106</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HDPK Dharmasena</td>
      <td>87</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C Shamshuddin</td>
      <td>73</td>
    </tr>
  </tbody>
</table>
</div>



<h3>Total number of ties in each season</h3>


```python
df2.query('result=="tie"')[['result','season']].groupby('season').count()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>result</th>
    </tr>
    <tr>
      <th>season</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2009</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>

