#! /usr/bin/env python3
'''
Apply an arbitrary filter to each docstring
'''

import pdoc

substitutions = [
	('δ13C_VPDB', 'δ<sup>13</sup>C<sub>VPDB</sub>'),
	('δ18O_VPDB', 'δ<sup>18</sup>O<sub>VPDB</sub>'),
	('δ18O_VSMOW', 'δ<sup>18</sup>O<sub>VSMOW</sub>'),
	('δ13CVPDB', 'δ<sup>13</sup>C<sub>VPDB</sub>'),
	('δ18OVPDB', 'δ<sup>18</sup>O<sub>VPDB</sub>'),
	('δ18OVSMOW', 'δ<sup>18</sup>O<sub>VSMOW</sub>'),
	('δ13C', 'δ<sup>13</sup>C'),
	('δ18O', 'δ<sup>18</sup>O'),
	('12C', '<sup>12</sup>C'),
	('13C', '<sup>13</sup>C'),
	('16O', '<sup>16</sup>O'),
	('17O', '<sup>17</sup>O'),
	('18O', '<sup>18</sup>O'),
	('δ4x', 'δ<sub>4x</sub>'),
	('δ45', 'δ<sub>45</sub>'),
	('δ46', 'δ<sub>46</sub>'),
	('δ47', 'δ<sub>47</sub>'),
	('δ48', 'δ<sub>48</sub>'),
	('δ49', 'δ<sub>49</sub>'),
	('Δ4x', 'Δ<sub>4x</sub>'),
	('Δ4x', 'Δ<sub>4x</sub>'),
	('Δ47', 'Δ<sub>47</sub>'),
	('Δ48', 'Δ<sub>48</sub>'),
	('Δ49', 'Δ<sub>49</sub>'),
	('χ2', 'χ<sup>2</sup>'),
	('χ^2', 'χ<sup>2</sup>'),
	('CO2', 'CO<sub>2</sub>'),
	]

def myfilter(docstr):
	work = docstr.split('```')
	for k in range(len(work)):
		if k:
			work[k] = work[k].lstrip('`')
		if k%2 == 0:
			work[k] = work[k].split('`')
			for j in range(len(work[k])):
				if not j%2:
					for x,y in substitutions:
						work[k][j] = work[k][j].replace(x,y)
			work[k] = '`'.join(work[k])
	return ('```'.join(work))

pdoc.render.env.filters['myfilter'] = myfilter
pdoc.render.configure(template_directory = 'pdoc_templates')

with open('docs/index.html', 'w') as fid:
	fid.write(pdoc.pdoc('D47crunch'))

# foo = '''
# Create foo δ13C bar Δ47 δ18O_VSMOW `δ13C_VPDB`, `Δ48`.
# 
# ````py
# Create foo δ13C bar `Δ47` δ18O_VSMOW.
# ```
# '''
# 
# print(myfilter(foo))