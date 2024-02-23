# B04-SurveyVote

PATH `http://192.168.56.110/index.php?page=survey#`

Pour celui-ci nous allons sur la page `survey` et on peux voir un systeme de vote.

En inspectant le code, on peux voir que les notes que nous mettons sont directement passer dans le code en tant que valeur, donc si on change cette valuer pour quelque chose de tres grand on peux fausser le vote.

On test

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

On modifie les values

```
<option value="1000000">10</option>
```

```
THE FLAG IS 03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA
```