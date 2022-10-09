import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
   # Read data from file
    data = pd.read_csv('./adult.data.csv')
    percentage = lambda x,y: np.round(x/(0.01*y),1)
    check = lambda x,y: ((x not in ['Bachelors','Masters','Doctorate'])^y)
  
    #race_count
    race_count = race_count = data[['race','age']].groupby(by=['race'],axis=0).count().values.reshape(-1)

    average_age_men = data[data['sex']=='Male'].age.mean().round(1)
  
    percentage_bachelors = percentage(data[data['education'] == 'Bachelors'].shape[0],data.shape[0])
    
    gth50k = data[data['salary'] == '>50K']

    higher_education_rich = percentage(gth50k['education'].apply(func = check,args=[True]).sum(),data['education'].apply(func = check,args=[True]).sum())
    lower_education_rich = percentage(gth50k['education'].apply(func = check,args=[False]).sum(),data['education'].apply(func = check,args=[False]).sum())

  
    min_work_hours = data['hours-per-week'].values.min()
    rich_percentage = percentage(gth50k[gth50k['hours-per-week'] == min_work_hours ].shape[0],data[data['hours-per-week'] == min_work_hours ].shape[0])
  
    high_inc = percentage(gth50k.groupby('native-country').count().age,data.groupby('native-country').count().age)
    high_inc.fillna(0)
    highest_earning_country = high_inc.idxmax()
    
    highest_earning_country_percentage = high_inc.max()
    top_IN_occupation = gth50k[gth50k['native-country'] == 'India'].groupby('occupation').age.count().idxmax()
    
    return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage':
      highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
    }