'''
Python 2.7
The clustergrammer python module can be installed using pip:
pip install clustergrammer

or by getting the code from the repo:
https://github.com/MaayanLab/clustergrammer-py
'''

from clustergrammer import Network
net = Network()

# load matrix tsv file
net.load_file('../data_mats/df_predict_merge.txt')

net.set_cat_color('row', 1, 'virus: chik', 'blue')
net.set_cat_color('row', 1, 'virus: zika', 'red')
net.cluster(enrichrgram=False)

# transfer colors from original to predicted categories
########################################################

# make category colors the same for Chik groups
for inst_cat in net.viz['cat_colors']['row']['cat-1']:
    new_cat = inst_cat.replace('original','predict')
    inst_color = net.viz['cat_colors']['row']['cat-1'][inst_cat]
    net.set_cat_color('row', 3, new_cat, inst_color)

net.cluster(enrichrgram=False)

# write jsons for front-end visualizations
net.write_json_to_file('viz', 'json/mult_view.json', 'indent')
# net.write_json_to_file('sim_row', 'json/mult_view_sim_row.json', 'no-indent')
# net.write_json_to_file('sim_col', 'json/mult_view_sim_col.json', 'no-indent')
