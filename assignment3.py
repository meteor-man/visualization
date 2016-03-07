import pandas as pan
import matplotlib
matplotlib.use('Qt4Agg')
from matplotlib import pyplot as plt
import seaborn as sns
sns.set(style="ticks", palette="muted", color_codes=False)

def show_figure(plt):
    plt.get_current_fig_manager().window.raise_()
    plt.show()

def show_salaries_boxplot(df):
    ax = sns.boxplot(x="University", y="Annual_Salary", data=df, color="c")
    #ax.set_yscale("log")
    ax.set_ylabel('Annual Salary ($)')
    sns.despine(trim=True)
    show_figure(plt)

def show_emps_barplot(df):
    g = sns.factorplot(x='University', data=df, kind="count",palette="BuPu", size=6, aspect=1.5,)
    g.set_ylabels("Number of Salaried Employees")
    show_figure(plt)

def show_salary_hist(df,univ_name='NCF'):
    ax = sns.distplot(df[df.University==univ_name].Annual_Salary.values.tolist())
    ax.set_title('{} Salaries Histogram'.format(univ_name))
    show_figure(plt)

def show_median_by_school(df):
    grouped_data = df.groupby('University')['Annual_Salary'].median()
    my_plot = grouped_data.sort_values().plot(kind='bar',legend=None,title="Median Salary by University")
    my_plot.set_xlabel("University")
    my_plot.set_ylabel("Salary ($)")
    show_figure(plt)

def compare_fac_admin(df):
    fac = df.Class_Title.map(lambda x: x in ('ASSISTANT PROFESSOR','ASSOCIATE PROFESSOR','PROFESSOR','INSTRUCTOR','OFFICE ADMINISTRATOR','ADMINISTRATIVE SPECIALIST','EXECUTIVE SECRETARY','ADMINISTRATIVE ASSISTANT'))
    fac = df[fac]
    grouped_data = fac.groupby('Class_Title',sort=False)['Annual_Salary'].median()
    my_plot = grouped_data.sort_values().plot(kind='barh',legend=None,title="Median Salary by Position")
    my_plot.set_ylabel("Title")
    my_plot.set_xlabel("Salary ($)")
    show_figure(plt)

if __name__=='__main__':
    emp_df = pan.read_csv('../data/emp.csv')
    emp_df.columns = ['University', 'Budget_Entity', 'Position_Number', 'Last_Name',
       'First_Name', 'MI', 'Employee_Type', 'FTE', 'Class_Code',
       'Class_Title', 'Annual_Salary', 'OPS_Term_Amount']
    emp_df = emp_df[~(emp_df['Annual_Salary'].isnull())]
    emp_df['Class_Code'] = emp_df['Class_Code'].astype(str)
    #show_salaries_boxplot(emp_df)
    #show_emps_barplot(emp_df)
    #show_salary_hist(emp_df,univ_name='NCF')
    #show_salary_hist(emp_df,univ_name='USF')
    #show_median_by_school(emp_df)
    #show_median_by_position(emp_df)
    
    compare_fac_admin(emp_df)      
    