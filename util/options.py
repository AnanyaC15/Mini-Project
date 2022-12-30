import argparse

def train_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", default=100, type=int, help='')
    parser.add_argument("-predictionmodel", default=100, type=str, help='number of estimators')
    parser.add_argument("--parameters", default=6, type=int, help='maximum of features',)
  
	parser.add_argument('--dim_red_type', default='pca', choices=[
	  		    'pca','lle'], help='The dim red. types')
	parser.add_argument('--n_comp', default=10,type=int, choices=[
	 		     5,10], help='output dimensions')
	parser.add_argument('--classifier', default='lr', choices=[
			    'lr','svc','rf'], help='Classifiers')

    opt = parser.parse_args()
    return opt
