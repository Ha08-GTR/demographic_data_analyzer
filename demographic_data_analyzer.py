import pandas as pd
def calculate_demographic_data():
    df = pd.read_csv('adult_data_cleaned.csv')


    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[advanced_education]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[~advanced_education]['salary'] == '>50K').mean() * 100, 1)
    min_work_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)
    
    country_stats = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()) * 100
    country_stats = country_stats.fillna(0) 
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)
    filtered_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    if not filtered_df.empty:
        top_IN_occupation = filtered_df['occupation'].value_counts().idxmax()
    else:
        top_IN_occupation = 0  

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

if __name__ == "__main__":
    data = calculate_demographic_data()
    print(data)