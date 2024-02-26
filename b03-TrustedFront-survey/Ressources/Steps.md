# B03-TrustedFront-SurveyVote

##  BREACH

PATH `http://192.168.56.110/index.php?page=survey#`

For this one, we go to the `survey` page and we can see a voting system.

Inspecting the code, we can see that the ratings we input are directly passed into the code as values, so if we change this value to something very large, we can manipulate the vote.

We test


```
<tr bgcolor="Silver">
				<td align="center">
				<form action="#" method="post">
					<input type="hidden" name="sujet" value="4">
					<select name="valeur" onchange="javascript:this.form.submit();">
						<option value="1">1</option>
						<option value="2">2</option>
						<option value="3">3</option>
						<option value="4">4</option>
						<option value="5">5</option>
						<option value="6">6</option>
						<option value="7">7</option>
						<option value="8">8</option>
						<option value="9">9</option>
						<option value="10">10</option>
					</select>
				</form>
			</td>
			<td align="center"> 9.37838			</td>
			<td align="center"> Thor			</td>
			<td align="center"> 37			</td>
		</tr>
```

We modify the values

```
<option value="1000000">10</option>
```

```
THE FLAG IS 03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA
```

## PATCH

When building a website, a major rule is to never trust the front end with important data because the user can easily modify it as they wish.

Here, the value sent is directly used to impact the voting results, so the user can easily modify it. To fix this, simply perform a check in the backend to ensure that the values are within the possible range, i.e., between `1 and 10`.