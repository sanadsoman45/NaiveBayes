import pandas as pd
def naive_pred_bayes(alt,bar,fri_sat,Hungry,Patrons,Price,Raining,reservation,Type,wait_Estimate):
    hotels=pd.read_excel("<File_path>")
    print(hotels.to_string())
    hotels.head(5)
    total_yes=len(hotels[(hotels["Ans"]=="yes")])
    total_no=len(hotels[(hotels["Ans"]=="no")])
    total_p_yes=len(hotels[(hotels["Alternate"]=="yes") & (hotels["Ans"]=="yes")])/total_yes+len(hotels[(hotels["Alternate"]=="no") & (hotels["Ans"]=="yes")])/total_yes
    total_p_no=len(hotels[(hotels["Alternate"]=="yes") & (hotels["Ans"]=="no")])/total_no+len(hotels[(hotels["Alternate"]=="no") & (hotels["Ans"]=="no")])/total_no

    def generate_subtable(feaure_name):
        dta = [(len(hotels[(hotels[feaure_name]=="yes") & (hotels["Ans"]=="yes")]),len(hotels[(hotels[feaure_name]=="yes") & (hotels["Ans"]=="no")]),len(hotels[(hotels[feaure_name]=="yes") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels[feaure_name]=="yes") & (hotels["Ans"]=="no")])/total_no),
        (len(hotels[(hotels[feaure_name]=="no") & (hotels["Ans"]=="yes")]),len(hotels[(hotels[feaure_name]=="no") & (hotels["Ans"]=="no")]),len(hotels[(hotels[feaure_name]=="no") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels[feaure_name]=="no") & (hotels["Ans"]=="no")])/total_no),
        (total_yes,total_no,total_p_yes,total_p_no)]
        return dta
    print("\n\n**Alternate data*")
    sub_data=generate_subtable("Alternate")
    alternate_dataframe=pd.DataFrame(sub_data,columns=["Yes","No","P(YES)","P(NO)"],index=["yes","no","Total"])
    print(alternate_dataframe)
    print("\n\n**Bar data*")
    sub_data=generate_subtable("Bar")
    Bar_dataframe=pd.DataFrame(sub_data,columns=["Yes","No","P(YES)","P(NO)"],index=["yes","no","Total"])
    print(Bar_dataframe)
    print("\n\n**Fri/Sat data*")
    sub_data=generate_subtable("Fri/Sat")
    Fri_Sat_dataframe=pd.DataFrame(sub_data,columns=["Yes","No","P(YES)","P(NO)"],index=["yes","no","Total"])
    print(Fri_Sat_dataframe)
    print("\n\n**Hungry data*")
    sub_data=generate_subtable("Hungry")
    Hungry_dataframe=pd.DataFrame(sub_data,columns=["Yes","No","P(YES)","P(NO)"],index=["yes","no","Total"])
    print(Hungry_dataframe)
    print("\n\n**Patrons data*")
    sub_data=[(len(hotels[(hotels["Patrons"]=="some") & (hotels["Ans"]=="yes")]),len(hotels[(hotels["Patrons"]=="some") & (hotels["Ans"]=="no")]),len(hotels[(hotels["Patrons"]=="some") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels["Patrons"]=="some") & (hotels["Ans"]=="no")])/total_no),
    (len(hotels[(hotels["Patrons"]=="full") & (hotels["Ans"]=="yes")]),len(hotels[(hotels["Patrons"]=="full") & (hotels["Ans"]=="no")]),len(hotels[(hotels["Patrons"]=="full") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels["Patrons"]=="full") & (hotels["Ans"]=="no")])/total_no),
    (len(hotels[(hotels["Patrons"] == "None") & (hotels["Ans"] == "yes")]),
               len(hotels[(hotels["Patrons"] == "none") & (hotels["Ans"] == "no")]),
               len(hotels[(hotels["Patrons"] == "none") & (hotels["Ans"] == "yes")]) / total_yes,
               len(hotels[(hotels["Patrons"] == "none") & (hotels["Ans"] == "no")]) / total_no),

              (total_yes,total_no,total_p_yes,total_p_no)]
    Patrons_dataframe=pd.DataFrame(sub_data,columns=["Yes","No","P(YES)","P(NO)"],index=["some","full","none","Total"])
    print(Patrons_dataframe)
    print("\n\n**Price data*")
    sub_data=[(len(hotels[(hotels.iloc[0:,5]=="high") & (hotels["Ans"]=="yes")]),len(hotels[(hotels.iloc[0:,5]=="high") & (hotels["Ans"]=="no")]),len(hotels[(hotels.iloc[0:,5]=="high") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels.iloc[0:,5]=="high") & (hotels["Ans"]=="no")])/total_no),
    (len(hotels[(hotels.iloc[0:,5]=="medium") & (hotels["Ans"]=="yes")]),len(hotels[(hotels.iloc[0:,5]=="medium") & (hotels["Ans"]=="no")]),len(hotels[(hotels.iloc[0:,5]=="medium") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels.iloc[0:,5]=="medium") & (hotels["Ans"]=="no")])/total_no),
    (len(hotels[(hotels.iloc[0:,5]=="low") & (hotels["Ans"]=="yes")]),len(hotels[(hotels.iloc[0:,5]=="low") & (hotels["Ans"]=="no")]),len(hotels[(hotels.iloc[0:,5]=="low") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels.iloc[0:,5]=="low") & (hotels["Ans"]=="no")])/total_no),
    (total_yes,total_no,total_p_yes,total_p_no)]
    Price_dataframe=pd.DataFrame(sub_data,columns=["Yes","No","P(YES)","P(NO)"],index=["high","medium","low","Total"])
    print(Price_dataframe)
    print("\n\n**Type*")
    sub_data=[(len(hotels[(hotels["Type"]=="french") & (hotels["Ans"]=="yes")]),len(hotels[(hotels["Type"]=="french") & (hotels["Ans"]=="no")]),len(hotels[(hotels["Type"]=="french") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels["Type"]=="french") & (hotels["Ans"]=="no")])/total_no),
    (len(hotels[(hotels["Type"]=="thai") & (hotels["Ans"]=="yes")]),len(hotels[(hotels["Type"]=="thai") & (hotels["Ans"]=="no")]),len(hotels[(hotels["Type"]=="thai") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels["Type"]=="thai") & (hotels["Ans"]=="no")])/total_no),
    (len(hotels[(hotels["Type"]=="burger") & (hotels["Ans"]=="yes")]),len(hotels[(hotels["Type"]=="burger") & (hotels["Ans"]=="no")]),len(hotels[(hotels["Type"]=="burger") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels["Type"]=="burger") & (hotels["Ans"]=="no")])/total_no),
    (len(hotels[(hotels["Type"]=="italian") & (hotels["Ans"]=="yes")]),len(hotels[(hotels["Type"]=="italian") & (hotels["Ans"]=="no")]),len(hotels[(hotels["Type"]=="italian") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels["Type"]=="italian") & (hotels["Ans"]=="no")])/total_no),
    (total_yes,total_no,total_p_yes,total_p_no)]
    Type_dataframe=pd.DataFrame(sub_data,columns=["Yes","No","P(YES)","P(NO)"],index=["french","thai","burger","italian","Total"])
    print(Type_dataframe)
    print("\n\n**Estimate Time*")
    sub_data=[(len(hotels[(hotels["wait Estimate"]=="0-10") & (hotels["Ans"]=="yes")]),len(hotels[(hotels["wait Estimate"]=="0-10") & (hotels["Ans"]=="no")]),len(hotels[(hotels["wait Estimate"]=="0-10") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels["wait Estimate"]=="0-10") & (hotels["Ans"]=="no")])/total_no),
    (len(hotels[(hotels["wait Estimate"]=="30-60") & (hotels["Ans"]=="yes")]),len(hotels[(hotels["wait Estimate"]=="30-60") & (hotels["Ans"]=="no")]),len(hotels[(hotels["wait Estimate"]=="30-60") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels["wait Estimate"]=="30-60") & (hotels["Ans"]=="no")])/total_no),
    (len(hotels[(hotels["wait Estimate"]==">60") & (hotels["Ans"]=="yes")]),len(hotels[(hotels["wait Estimate"]==">60") & (hotels["Ans"]=="no")]),len(hotels[(hotels["wait Estimate"]==">60") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels["wait Estimate"]==">60") & (hotels["Ans"]=="no")])/total_no),
    (len(hotels[(hotels["wait Estimate"]=="10-30") & (hotels["Ans"]=="yes")]),len(hotels[(hotels.iloc[0:,9]=="10-30") & (hotels["Ans"]=="no")]),len(hotels[(hotels.iloc[0:,9]=="10-30") & (hotels["Ans"]=="yes")])/total_yes,len(hotels[(hotels.iloc[0:,9]=="10-30") & (hotels["Ans"]=="no")])/total_no),
    (total_yes,total_no,total_p_yes,total_p_no)]
    time_estimate_dataframe=pd.DataFrame(sub_data,columns=["Yes","No","P(YES)","P(NO)"],index=["0-10","30-60",">60","10-30","Total"])
    print(time_estimate_dataframe)
    print("\n\n**Raining data*")
    sub_data=generate_subtable("Raining")
    Raining_dataframe=pd.DataFrame(sub_data,columns=["Yes","No","P(YES)","P(NO)"],index=["yes","no","Total"])
    print(Raining_dataframe)
    print("\n\n**Reservation data*")
    sub_data=generate_subtable("Reservation")
    Reservation_dataframe=pd.DataFrame(sub_data,columns=["Yes","No","P(YES)","P(NO)"],index=["yes","no","Total"])
    print(Reservation_dataframe)
    print("\n\n**Ans data*")
    sub_data=[(total_yes,total_yes/(total_yes+total_no)),
              (total_no,total_no/(total_no+total_yes)),
              (total_no+total_yes,total_no/(total_no+total_yes)+total_yes/(total_yes+total_no))
             ]
    Ans_dataframe=pd.DataFrame(sub_data,columns=["Play","P(YES)/P(NO)"],index=["yes","no","Total"])
    print(Ans_dataframe)
    Ans=["YES","NO"]
    list_dem=[]
    tp="yes"
    for i in range(0,len(Ans)):
            print("Alternate is:"+alt+'P('+Ans[i]+')')
            print("bar is:"+bar+'P('+Ans[i]+')')
            print("fri_sat is:"+fri_sat+'P('+Ans[i]+')')
            print("Hungry"+Hungry+'P('+Ans[i]+')')
            print("Patrons"+Patrons+'P('+Ans[i]+')')
            print("Price"+Price+'P('+Ans[i]+')')
            print("Raining"+Raining+'P('+Ans[i]+')')
            print("reservation"+reservation+'P('+Ans[i]+')')
            print("Type"+Type+'P('+Ans[i]+')')
            print("wait_Estimate"+wait_Estimate+'P('+Ans[i]+')')
            alt_data=alternate_dataframe.at[alt,'P('+Ans[i]+')']
            bar_data=Bar_dataframe.at[bar,'P('+Ans[i]+')']
            fri_sat_data=Fri_Sat_dataframe.at[fri_sat,'P('+Ans[i]+')']
            Hungry_data=Hungry_dataframe.at[Hungry,'P('+Ans[i]+')']
            Patrons_data=Patrons_dataframe.at[Patrons,'P('+Ans[i]+')']
            Price_data=Price_dataframe.at[Price,'P('+Ans[i]+')']
            Raining_data=Raining_dataframe.at[Raining,'P('+Ans[i]+')']
            reservation_data=Reservation_dataframe.at[reservation,'P('+Ans[i]+')']
            Type_data=Type_dataframe.at[Type,'P('+Ans[i]+')']
            wait_Estimate_data=time_estimate_dataframe.at[wait_Estimate,'P('+Ans[i]+')']
            print(alt_data,bar_data,fri_sat_data,Hungry_data,Patrons_data,Price_data,Raining_data,reservation_data,Type_data,wait_Estimate_data)
            list_dem.append((alt_data*bar_data*fri_sat_data*Hungry_data*Patrons_data*Price_data*Raining_data*reservation_data*Type_data*wait_Estimate_data)*Ans_dataframe.at[tp,"P(YES)/P(NO)"])
            tp="no"
            
    print("probability yes = ",list_dem[0],"probability no = ",list_dem[1])
    if(list_dem[0]+list_dem[1]!=1):
        pr_y = list_dem[0]/(list_dem[0]+list_dem[1])
        print("Probability of yes = ",pr_y)
        pr_n = list_dem[1]/(list_dem[0]+list_dem[1])
        print("Probability of no = ",pr_n)
        if(pr_y>pr_n):
            print("You will wait")
        else:
            print("You will not wait")
    else:
        if(pr_y>pr_n):
            print("Probability of yes = ",list_dem[0])
            print("You will wait")
        else:
            print("Probability of no = ",list_dem[1])
            print("You will not wait")
alt=input("Is there any other restaurant available? ").lower()
bar=input("Do you want Bar? ").lower()
fri_sat=input("Is it a Weekend? ").lower()
Hungry=input("Are You Hungry? ").lower()
Patrons=input("How many customers are there? ").lower()
Price=input("What is the Price? ").lower()
Raining=input("Is it Raining? ").lower()
reservation=input("Do you have Reservation? ").lower()
Type=input("Which cuisine do you want? ").lower()
wait_Estimate=input("What is the waiting time? ").lower()
naive_pred_bayes(alt,bar,fri_sat,Hungry,Patrons,Price,Raining,reservation,Type,wait_Estimate)
