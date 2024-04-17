import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

import asyncio
import os
from sydney import SydneyClient

st.set_page_config(
    page_title="Doc Assist",
    page_icon="🥼",
)

st.markdown("# Heart Attacks Can Attack Anyone")

heart = pd.read_csv('C:/Users/shree/Documents/Disease/heart_1.csv')

# Column name replacements
replace = {
    'age': 'Age',
    'sex': 'Sex',
    'cp': 'Chest_Pain',
    'trestbps': 'Resting_Pressure',
    'chol': 'Cholesterol',
    'fbs': 'Fasting_Blood_Sugar',
    'restecg': 'Resting_Ecg_Results',
    'thalach': 'Maximum_Heart_Rate',
    'exang': 'Exercise_Induced_Angina',
    'oldpeak': 'Old_Peak',
    'slope': 'Slope',
    'ca': 'Major_Vessels',
    'thal': 'Thallium_Rate',
    'target': 'Target'
}

# Apply column name replacements
heart.rename(columns=replace, inplace=True)

# Plotting
plt.figure(figsize=(10,10))
sns.distplot(heart[heart['Target'] == 0]["Age"], color='green',kde=True,) 
sns.distplot(heart[heart['Target'] == 1]["Age"], color='red',kde=True)
plt.title('Attack versus Age')
plt.xlabel('Age')
plt.ylabel('Density')
st.pyplot(plt)

# Quiz Section
st.markdown("## Lifestyle Quiz")
st.write("Answer the following questions to get personalized lifestyle recommendations:")

# Physical Activity
physical_activity = st.radio("How often do you engage in physical activity?", options=["Sedentary", "Light exercise", "Moderate exercise", "Intense workouts"])
fav_physical = st.text_input("What physical activity do you enjoy the most? (Eg: Swimming, Hiking, Dancing, etc.)")
# Current Health Conditions
health_conditions = st.text_input("Do you have any existing health conditions? (e.g., diabetes, hypertension, cholesterol)")
medications = st.text_input("Are you taking any medications? (Please specify)")

# Dietary Preferences
diet_type = st.radio("What type of diet do you follow?", options=["Vegetarian", "Vegan", "Omnivore"])
diet_restrictions = st.text_input("Any dietary restrictions or allergies? (e.g., gluten-free, lactose intolerance)")
food_preferences = st.text_input("Any specific foods you love or dislike?")
meal_times = st.text_input("When do you typically have your meals? (e.g., breakfast, lunch, dinner)")
cooking_skills = st.radio("How comfortable are you with cooking?", options=["Novice", "Intermediate", "Expert"])

# Stress Management
stress_management = st.radio("How do you manage stress?", options=["Meditation", "Exercise", "Socializing"])

# Sleep Patterns
sleep_hours = st.number_input("How many hours of sleep do you get on average?", min_value=0)

# Hydration
hydration = st.radio("How much water do you drink daily?", options=["Less than 4 glasses", "4-8 glasses", "More than 8 glasses"])

# Social Support
social_support = st.text_input("Do you have a support system for maintaining heart health? (e.g., family, friends, online communities)")

# Other
smoke = st.radio("Do you smoke?", options=["Yes, regularly", "Yes, occasionally", "No, but I used to", "No, but I'm trying to quit", "No, never"])

os.environ["BING_COOKIES"] = "_C_Auth=; MUID=23A69D5D8931661C33AF8E2388436701; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=CCB87F92AAB94B14A494B1A9C2DF0A2E&dmnchg=1; SRCHS=PC=HCTE; _Rwho=u=d; BFBUSR=BAWAS=1&BAWFS=1; BFB=AxDfjiyceYvv8eeEGJGOrpsgyE-CHxfvsjc2x7vXnsW15v6wwvJXI1DQar96y8OcHfeFS18RTonw2HMV9VCt2O7dKt6aNDvG45KN0qH3cHKiLzlUblavwSXCxuUPXWPZ2SxAPgawgL-QhBfUChErhPjSzpuWCW0N1x_1B1aIjvq6VPIabRY4rMZVeztPgpgZSU8; _BINGNEWS=SW=1517&SH=862; MUIDB=23A69D5D8931661C33AF8E2388436701; _UR=cdxcls=0&QS=0&TQS=0; OIDR=gxAsY_WkD2x5kN42sJkK-3WcOtYaayyUQhLraub-mRFEHIACxk_k4Vc7Lk-0epYMtaACx9A1H1g920vPT0m0DqUyk-woQ1_bkZov9TNsPzGvNjYyDhmUQG3cWhezWwCE8ds3vCAJPUJgL4MKWVJjefcSb3jKRNdVdsuux8T5Pwl2Im70w5Kmg5tJbkJhr7E3JnUCCIqUOZotpZ-QkhzATEtGqWdIpw6SGTRJCqLGO7yzcipoiuo9udFgzvt_fx2dIEdAxmCCJz3Mz9p46EREM3mVqYJzJz9MrB-6t8_vp1kZO8TXi7iQMuIwTKclxYS9DnYyrXipdIolsl6ir9VpfNUr2xXvO6H-bbv9Me0ibmXn_bZpDEsOZDFLjrtq6pqTVtUgeEljmTBk2CJh4Dyjv5hGlGlfCbORf69MkWwAekr8NWD4E5sG2AptOffjgSSDexM8-HaOU5vvIJsM-uAeGW0n2XqgySUrAcwZmXPLAp8SqGuaqwjv83Gor1Uuq72XPhNLieAHRpNr0Gas2RQfSSt6CZrnj1yixURldw-t95hDkEWjblgAQ4kwUOomWldlkHpvO5237jsrmiVC_HXEX8LIgKmwyAeN0tOJb_N2qGONidKWhU20MfsiYjMAXCpmG5StX1rJRMJOWhiwqOJJfO-eKBmOBnYF2NOIWdsldOVVPbp0e8QmGumAUVlHxqe1N2mA-M0OPqsldhO8yQXWDt9LvCrYIFVhNBjgg4XFpp2foU7QPRKFvhKwgFjEROiITkQ403JMlSmxxB2CKNIQZE1O3ogPOOMwODB966axmUd7kzyLU8Vgq6QittiTUfic2uP80p29yvjk3ncfpM252d4z1mqyke7mqghY56Wme5dL-ydJgVGhcithaTc_ynsKusIrrGEN1_FqkDWsAvj_Y-JXQYdtShZxxO1UE9EVPwwl6HIlQuYhHBJRiPnlR2BJYr6iwNOG2S-sbqYu4hvmTek4nCQRs_5QPIz6F2PUjY6j611zGxkNFgXTTn0p7n-VIIXjzwGzfMiSY0fIwNqGv5Mr; ACL=AxA2NZdvftJyWE1ew7uj54s_fncicExe0JxY9wHJ6w1N0IsnDTJIx-KfMtSUM1vFViGM4oHO4yG-cHRVxL4vb_Wk; ACLUSR=T=1708393828000; ReturnUrl=https%3a%2f%2fwww.bing.com%2fwebmaster%2ftools; MSCC=NR; CSRFCookie=83037ef9-603a-492a-be00-c3947994a8bf; ANON=A=B4D03B8E872FD12C2BEDB21BFFFFFFFF&E=1d6f&W=1; NAP=V=1.9&E=1d15&C=BznrEs5HQEEDgC0M6-RDJzOUMWMN_Q1YrPX4Ikc3SR-cTI7fOxNYCA&W=1; PPLState=1; KievRPSSecAuth=FAB6BBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACFWeBCibEiZ5OAREBZuD3Fx98memvB3X1norEbZZwnBzWks4jRI0GfVNTbdJwFnfr+Tvx/roktGRPcqTy99U8MUeHk3njJzDDGwXy5ss54IDdbTCmgjxniZYNryXp1266hc+wPj3LBpiDOqAbb7lx+UaNtCsZBN6/kMr5CO8sMkTfYNTySQWq7kfiwX2au/oLF9Eh/4DQZeAdX7n0iG7ySFuUygiGdBezJHZ/Nr2EiKzXzURTafRt1Pg9vJlYsVDMu24dTiawX05NYOEH0tcjDaqjWaQ/u5lQz86WaQd7ycxu5vbSWnBTu3wDsw1ooNnlBxEjb5mYWXIIFgd15wgnbfTSKAkddLVgSWOaEfLgv63/kXTIiyJ2VGx4svLe4H2PVvLo1AcN51tZ6ndHPWY2JAfGsa8zAFlYUuCbxflYx/8Au0mtjdhJoZ9zK50DDniMeI+MTb3Bk+Y1x3q73KthZ2gCfmM890u9CSzIgMsrE+j6mOB2x1QKOq7aEXrWoT5PlypqYHzf0LYjmM8mQ8ldgMAe2R2ckA1YQPUBFGC6fWZESZ1OK5MOgWdys3GoUGEDnk6YhJFlrmSx/hdEqCp2Nht5aGvA7XJcGovl2/vA7CfdFT4uap712Qhpk911VSCL/dGNjy0Rz0OQPP8KasR8SknWYG7LN1ZYDH9oJMyesHIgnAhUWYlIBRjN4J2WYmc5YZRYtnoqhjtad9WED/B/DO3m3Naa4am+6uKRaud4altO/ZMlt+oiXLUw0fBVCac4wQ5YSg54jKc05SW8bCMpfWPpBAkk/0bYIKMD9M2Sa/vqz43rxMRLncYVoAzLC8nc125T4s3/6+s1BFILNmmzcoW+WYtaskShpNUOBSDuDVR09GNzjAZ7BUhho9UfrkuuYZgC2jz+QQpwz6ns7caqAODttQ4BroiLTzCbd0KvtHZBrNw6eGqy1gW40jmCYxDKkpwmnYmse2Sug5+ZwE6K0NOShHZPi+jNVs6s5lfQMdip1A1gsMvpUE/EHrWGHdVSF8YOygKNOqjBxJkeY+6VaSSME55t/pHDAwe9T8y+fX4aww5ewQxKLT6wFmxvZ+6wI3Z30hGyucOPJoeUXqpoRfd2647T1Vi5kZfqqwxcW4iADPsUHaTqM7xOVCK59GWzD4vVrZA/Ma9x7WizVZlHirbWlg0aNyNzwyHMgHGB98G6H6jm1efmV1x4eWGtfWS8+9Du0FqIrk8JBGWq9tv69tAToxEVBrSZnzoJB8x7Z6NCLUNVygC/E2WzO11+ZHpwStc1uis/z74BOmQWjNdEYQVIpoYalbqH2QytSJn8CpzQ4wp+cB/cqcM5QM6p30o1xRKfGvP1ecb0vBggOeawd1m/xRnsqe0D8sXOZsU//m+tbBZAVXOwWl3iVPUhfJGI5EFZ01J/DVCK/5dgxbDLG2YIwwwH6GT5eJFLw/HTAwkDzIUAA5FaEy4aUjl9CZzvE2VRJpxhNXS; _U=1eOu_fkhMg6c5CHM3Fj98VxaQjur0YpE1KivyzibvRQ8q-Df_O1fMTMSa-imuKosQ13RwoaTX7PSuhhQ_ZaUwY3O3ujRVudKQBsMBLzWeCV3EwwX_bzu3Ym0ft2aa37mO1YF_WHntO0nUOtv-33cnM7TUeZ_aqItl2P_GN2Odc5SjItvi5aktXPp2sedDmZX-wXiT9pR2ce_Bb87y20gnmMbYaY6vV65NHe2lpWzvaHI; WLS=C=0196c003a2609b93&N=Shreeja; WLID=NCZJ5SK+OkEpRtVcLEw+ZlBL6gWz7YS3KuegetvnPMttV8ZEc/yF+88/3CSlfqIPpFlQumc//HMfAJ94d3J1R/qroAd53yLXs+PiXMX00Bw=; SnrOvr=X=rebateson; _SS=SID=0B1B737CDB67650C073C60B1DAED646B&PC=HCTE&R=120&RB=120&GB=0&RG=0&RP=120; MicrosoftApplicationsTelemetryDeviceId=9bdc600d-d50e-4296-8d98-d8431a5084b2; _EDGE_S=SID=1DB3586448426DFA23144C4F49B26C69&mkt=en-us&ui=en-us; ipv6=hit=1708447264088&t=4; SRCHUSR=DOB=20231118&T=1701719409000&TPC=1708444963000&POEX=W; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wMi0yMFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoxOSwiVG9ibiI6MH0=; ai_session=eDtZgCHtHDGXuBPuTV8kKI|1708443663984|1708445288817; USRLOC=HS=1&ELOC=LAT=41.03900146484375|LON=-74.22779846191406|N=Oakland%2C%20New%20Jersey|ELT=4|; OID=AxAVxnlw-5AccUhla40kaQIC8Ry7c5U0UVbPvIf9tYBfoOP07t_Ie5kf34zEhD9t82B5ZY-iExm8PlbvW6nkm-q11bGr3BpO401JuRKEHyC8SJi3i2SfsZ1GofuJ1ZYl6Ublc3dAyJF2xZtElBRL2CLQ; OIDI=gxA3hZ2oyxNTNAep5o4oF7Ug7EtYG72j-kx4QPDDzGjIoP7A2KFdn1S-1_lO28bfevw1uT4l8jEnhRrMoXG57KMb3YI-8zCKROP7_mql07qg_4n5zKJg-vcGl0Vga8pmJpavfL6zHt9vHeAGroMljhPNQATjVSO4RSiHK5LNKBu1nqO8H2cQ2D-M0ad4rL-v0RYs9ljQEmleDDr8vU_DzUTVm8HPXVT3DdaOEsBn_Qzb8xhfNYHmAMR6d7e-B4N61_07UA6HNWyvc8JJG3RgwC1rFosfCfN7rP4MR7MRIe6n3ccW47RNuDJgRxk_7rJU9PBOO1hYDkIYPivfJEciis5ZB1q152rSmPVyVMuxHUZRpKoXPhlBiYkYkIH_2kuL8g8ILB2gDWD43X7nvY2UWVp0a3Unsi6b49qApCAnvFs23toVrZ3SxvW7uNKxjTVbcOCMReH9iHxJIUYCIq4gLrkX4NBgXPpCn1C3glQfvnxiGTVZUmh6lBsEBUwQM20aCZV14Q_WREsj6jKn-OS1oI_SPhGu2c6IX_z6A_C_psRJyXvppXFeWU_clcYmqqD9Q-Xog_p-QWTzeJr0tHteTpJdANHbW-gNzjM1f8Au5CGqug-jQVgoF1sQVm4ZkkEQz-mrBnX4FYoOckUSXBamCZrWQEiaBrXv6koT5BW8QX97gH_3JRR84AI8TSpKsWivXpyf_3Cr1I3RXjSW8X-HpzBI2yaNZ5VYahTpXBRCAJgBinExnJ5GWZuod68aiDF1Qp2phnMSan3Qb3BfPeJDdKm1TtNg5b0u_c6Hm2Yul2JmX3AHtlDmRqaY4qSLk9VBVi6GIyo2A-B8EEiF8djJhpIrHfg8p6D1nYXfVUoIpV3IDHdQ1dhcIYN6hSwPgaxtNEIGPhdxI0R06V_xxSia-QJRyoKazS4NrgYPiHGotT7Ar_Fw2kh8ox5HMINRmRXsXuAtnr7xjaa-BRdrg5jkyvzZ5P-APnndecMYKLvYd3kndRtL7hin6uxJ9IehpioDvGNNKHSUZdpxkBWBiu9cJeFwxMpHR2d2BbGSxtnxz6SZPJCC3ndbZXl9u7NtSvi7e6anPba0C12xDuEeK94ZeeMfuRatKGGmc0alGq1L6u6nq4oBWV5Qv4OxtdIWP74ZvP8A9GRzP7oKQIU9COSlYvx9tnWpmVsh9vhzdzOxa0IaKgHf9g5a7A4QjYGN5tuGWtCDjiRx3qXTQbNxwjAiT9lRjP_mEcbNlFhfC_7pgcPGVaSWgSC80iYe2Ix2KUFLBVV6Ck0NRKh_ZF22kr4Wv5B98y6M4vhPJVcj5GCpbvfVmTaNaByIzNnvD3g1UjF7OIaRrEeTm90UBNCbbBDC0y3yzPdKAZdnn91_-i9VXwKCjnwK8PErhuOHhMkbp8CKkPyfLUZxo7xXdH6Pu79Cu0UdsoCXJuyM9AXAQdwfW0hjI1qcxMwxwLv1ggWMLAADjv2Ozou53HKDbyuIf-Qe1fOrtoe0AhBevacDbUV9ksBuv-ZXtmRgdkDWQG3JjoMWsWJyrhSXLcz9I2B6dUDBKEvurSYFUEhYe18Gkk12PLe601FeNffJjTheKJ3kWTWe0peRArpWBaN66nUihWC6ugG2ovD9FykyfAQK_QKgZ3j5d_09vtSN9iVF_dkIaFbp4PQs484cU4BBj3sX50pNlLUTeyjd606zTWeI2zVLXnyPKtIefQuq1ZSkwhkdbxL5_nLl5tZx7xwgE2j2NgwAE4RNdvN4hKlYdNixK4IBWIxQLhToP06Lq-sfPoaMqU7fGZk24KEYFqtFh25AIbO2YpOfwwPn58dB4kY8NXdSIEYr-hArzhmKBFvNithU9GRU3Zit5PiSbEuDpP_6xbtuoTh61qoBquo1qFfnMGV9b2vT_3HcRiJOoarFLCmq8LCVVbLhMngUUs0qLQbVwYrmVT-vPsWjNqXovRWGCHkBJoxDd6Jz_x2hwbmfTxzkaPyR3Vs; _RwBf=r=1&ilt=12&ihpd=4&ispd=2&rc=120&rb=120&gb=0&rg=0&pc=120&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=6&l=2024-02-20T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=BINGCOPILOTWAITLIST&c=MR000T&t=6290&s=2023-06-16T15:32:30.7955038+00:00&ts=2024-02-20T16:08:33.5903384+00:00&rwred=0&wls=2&wlb=0&ccp=0&lka=0&lkt=1&aad=0&TH=&ard=2024-02-19T17:51:01.6390000-08:00&wle=1&rwdbt=0001-01-01T16:00:00.0000000-08:00&rwflt=0001-01-01T16:00:00.0000000-08:00&mta=0&e=wpxO14uL4ZyccVvF7WqEsCwNRdQd_hLuuqkbEdrBUVoApgP03HUgfy-sLwqsmxdO-X4RIE61aJkSHOO21_pZ0Q&A=B4D03B8E872FD12C2BEDB21BFFFFFFFF; _C_ETH=1; dsc=order=Video; SRCHHPGUSR=SRCHLANG=en&IG=D8E5E2E37EFE464A8381756BB5E8FEC7&BRW=NOTP&BRH=M&CW=694&CH=730&SCW=694&SCH=112&DPR=1.3&UTC=-300&DM=0&PV=15.0.0&CIBV=1.1586.1&PRVCW=694&PRVCH=730&HV=1708445315&cdxupdttm=638439636487807602"

async def main(answers) -> str:
    async with SydneyClient() as sydney:
        question = 'Based on the preferences of this person, create a schedule, health guideline, recommended diet plan, and a smoking quit plan if they smoke. Alongisde provide recommendations for support groups to help him/her improve their heart health that is customized to their interests. Be sure to make the plan as customized to the interests of the person as possible: '+str(answers)
        response = await sydney.ask(question, citations=True)
        return response.encode('ascii', 'ignore').decode('ascii')

# Function to generate plan and download it
def generate_and_download_plan(answers):
    plan = asyncio.run(main(answers))
    with open("heart_health_plan.txt", "w") as file:
        file.write(plan)
    return "heart_health_plan.txt"


# Submit Button
if st.button("Submit"):
    answers = [physical_activity, fav_physical, diet_type, diet_restrictions, health_conditions, medications,
               stress_management, sleep_hours, hydration, meal_times, food_preferences, cooking_skills, social_support, smoke]

    # Lifestyle Tips Section
    st.markdown("## Generic Tips")
    st.write("1. Maintain a healthy diet --> fruits, vegetables, and whole grains.")
    st.write("2. Engage in regular physical activity --> walking, jogging, or swimming.")
    st.write("3. Quit smoking, limit alcohol, or other drugs.")
    st.write("4. Manage stress through relaxation techniques --> meditation or yoga.")
    st.write("5. Monitor your blood pressure, cholesterol levels, and weight regularly.")
    st.write("6. Get at least 7-8 hours of sleep per night.")
    st.write("7. Drink at least 8 glasses of water to stay hydrated.")

    st.markdown("## Personalized Plan")
    plan_file_path = generate_and_download_plan(answers)
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    st.success("Plan generated successfully!")
    st.markdown("## Download Plan")
    st.write("Click the button below to download your personalized plan.")
    if st.download_button(label="Download Plan", data=open(plan_file_path, "rb"), file_name="heart_health_plan.txt"):
        st.success("Plan downloaded successfully!")

