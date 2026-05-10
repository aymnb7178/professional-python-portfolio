import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meal Planner & Nutrition Tracker", page_icon="🍽️", layout="wide")

st.title("🍽️ Meal Planner & Nutrition Tracker")
st.markdown("### تخطيط وجباتك اليومية وتتبع التغذية")

# Sample meal database
meals = [
    {"name": "بيض مسلوق + خبز كامل", "calories": 350, "protein": 25, "carbs": 30, "fat": 15, "type": "Breakfast"},
    {"name": "شوفان مع فواكه", "calories": 280, "protein": 8, "carbs": 45, "fat": 6, "type": "Breakfast"},
    {"name": "سلطة دجاج مشوي", "calories": 450, "protein": 40, "carbs": 10, "fat": 25, "type": "Lunch"},
    {"name": "رز بني + سمك مشوي", "calories": 520, "protein": 35, "carbs": 55, "fat": 12, "type": "Lunch"},
    {"name": "سلطة خضراوات + توفو", "calories": 320, "protein": 18, "carbs": 20, "fat": 18, "type": "Dinner"},
    {"name": "دجاج مشوي + بطاطس مشوية", "calories": 480, "protein": 38, "carbs": 35, "fat": 20, "type": "Dinner"},
    {"name": "يوغورت يوناني + مكسرات", "calories": 200, "protein": 15, "carbs": 25, "fat": 5, "type": "Snack"},
    {"name": "تفاحة + لوز", "calories": 180, "protein": 5, "carbs": 25, "fat": 8, "type": "Snack"},
]

# Sidebar for user inputs
st.sidebar.header("الإعدادات الشخصية")
calorie_goal = st.sidebar.number_input("الهدف اليومي للسعرات", min_value=1000, max_value=4000, value=2000, step=50)

st.sidebar.subheader("تفضيلات التغذية")
protein_goal = st.sidebar.slider("Protein (g)", 50, 200, 100)
carbs_goal = st.sidebar.slider("Carbs (g)", 100, 400, 250)
fat_goal = st.sidebar.slider("Fat (g)", 40, 120, 70)

# Main area
col1, col2 = st.columns(2)

with col1:
    st.header("🍽️ Meal Suggestions")
    selected_type = st.selectbox("اختر نوع الوجبة", ["Breakfast", "Lunch", "Dinner", "Snack"])
    
    suggested = [m for m in meals if m["type"] == selected_type]
    if suggested:
        selected_meal = st.selectbox("اقتراح وجبة", [m["name"] for m in suggested])
        meal_info = next((m for m in suggested if m["name"] == selected_meal), None)
        if meal_info:
            st.write(f"**Calories:** {meal_info['calories']} kcal")
            st.write(f"Protein: {meal_info['protein']}g | Carbs: {meal_info['carbs']}g | Fat: {meal_info['fat']}g")
            
            if st.button("أضف إلى السجل اليومي"):
                if 'logged_meals' not in st.session_state:
                    st.session_state.logged_meals = []
                st.session_state.logged_meals.append(meal_info)
                st.success(f"تم إضافة {selected_meal} إلى السجل!")

with col2:
    st.header("📋 Daily Tracker")
    
    if 'logged_meals' not in st.session_state:
        st.session_state.logged_meals = []
    
    if st.session_state.logged_meals:
        df = pd.DataFrame(st.session_state.logged_meals)
        st.dataframe(df[['name', 'calories', 'protein', 'carbs', 'fat']])
        
        total_cal = df['calories'].sum()
        total_protein = df['protein'].sum()
        total_carbs = df['carbs'].sum()
        total_fat = df['fat'].sum()
        
        st.metric("Total Calories", f"{total_cal} / {calorie_goal} kcal", delta=f"{total_cal - calorie_goal}")
        st.metric("Protein", f"{total_protein}g / {protein_goal}g")
        st.metric("Carbs", f"{total_carbs}g / {carbs_goal}g")
        st.metric("Fat", f"{total_fat}g / {fat_goal}g")
        
        if st.button("مسح السجل اليومي"):
            st.session_state.logged_meals = []
            st.rerun()
    else:
        st.info("لم تضف أي وجبة بعد. استخدم الاقتراحات للإضافة!")

st.markdown("---")
st.caption("Project 2/60 - Professional Python Portfolio | Built with Streamlit")