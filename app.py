import streamlit as st

# 1. إعدادات الصفحة والتصميم
st.set_page_config(page_title="Eco-Digital Discussion Hub", layout="centered")

style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Cairo', sans-serif !important;
        color: #FFFFFF !important;
    }
    .stApp { background-color: #000000 !important; }
    h1, h2, h3, .stMetric label { color: #40E0D0 !important; font-weight: 700 !important; }
    .stButton>button {
        background-color: #40E0D0 !important; color: #000000 !important;
        border-radius: 12px !important; font-weight: bold !important; width: 100%;
    }
    .stSlider > div [data-baseweb="slider"] { background-color: #40E0D0 !important; }
    .stAlert { background-color: #111111 !important; border: 1px solid #40E0D0 !important; border-radius: 15px; }
    .discussion-card {
        background-color: #161616; padding: 20px; border-radius: 15px;
        border-right: 5px solid #40E0D0; margin-bottom: 20px;
    }
</style>
"""
st.markdown(style, unsafe_allow_html=True)

# 2. إدارة اللغة
if 'lang' not in st.session_state: 
    st.session_state.lang = 'عربي'

def switch(): 
    st.session_state.lang = 'English' if st.session_state.lang == 'عربي' else 'عربي'

# 3. محتوى الأسئلة والحقائق (تم التأكد من الفواصل بدقة)
content = {
    'عربي': {
        'btn': 'English 🌐',
        'title': 'مختبر الحساب البيئي الرقمي 🌍',
        'sub': 'لنقس أثرنا الرقمي ونحوله إلى قوة للتغيير',
        'q_email': 'كم إيميل ترسل يومياً؟',
        'q_news': 'كم "نشرة بريدية" أنت مشترك بها ولا تقرأها؟',
        'q_cloud': 'كم جيجابايت (صور/ملفات) مكدسة على السحابة ولا تحتاجها؟',
        'q_cam': 'ساعات الاجتماعات مع فتح الكاميرا يومياً؟',
        'q_ai': 'كم مرة تستخدم الذكاء الاصطناعي يومياً؟',
        'calc': 'استخراج النتائج وبدء النقاش 🚀',
        'res_title': 'تحليل أثرك الرقمي السنوي 📊',
        'unit': 'كيلوجرام CO2 سنوياً',
        'story_tree': 'هذا يعادل ما تمتصه حوالي {} أشجار في سنة كاملة!',
        'disc_header': 'محاور النقاش والمناصرة الرقمية 💡',
        'fact_jordan': 'الأردن يستورد طاقته؛ كل توفير رقمي هو دعم للاقتصاد والبيئة.',
        'fact_water': 'حصتك المائية شحيحة. تبريد مراكز البيانات يستهلك مياهك الثمينة.',
        'fact_green': 'احذر من التضليل الأخضر؛ ليس كل ادعاء بيئي صادقاً.',
        'advocacy_tip': 'المناصر الرقمي: ابدأ بحذف نفاياتك الرقمية أولاً.'
    },
    'English': {
        'btn': 'عربي 🌐',
        'title': 'Digital Eco-Lab 🌍',
        'sub': 'Measuring digital impact to drive real change',
        'q_email': 'Daily emails sent?',
        'q_news': 'Unread newsletter subscriptions?',
        'q_cloud': 'GBs of unneeded cloud files/photos?',
        'q_cam': 'Daily video meeting hours (Camera ON)?',
        'q_ai': 'Daily AI prompts used?',
        'calc': 'Generate Results & Start Discussion 🚀',
        'res_title': 'Your Annual Impact Analysis 📊',
        'unit': 'kg of CO2 per year',
        'story_tree': 'Equivalent to what {} trees absorb in a year!',
        'disc_header': 'Discussion Hub 💡',
        'fact_jordan': 'Jordan imports most of its energy. Efficiency supports the nation.',
        'fact_water': 'Water is scarce. Data center cooling uses your water!',
        'fact_green': 'Beware of Greenwashing in the tech world.',
        'advocacy_tip': 'Advocate: Clean your digital waste first.'
    }
}

l = st.session_state.lang
c = content[l]

# 4. واجهة المستخدم
col1, col2 = st.columns([7, 3])
with col1: 
    st.title(c['title'])
with col2: 
    st.button(c['btn'], on_click=switch)

st.write(f"*{c['sub']}*")
st.divider()

with st.expander("المدخلات الرقمية السلوكية / Digital Inputs", expanded=True):
    emails = st.slider(c['q_email'], 0, 150, 10)
    newsletters = st.slider(c['q_news'], 0, 50, 5)
    cloud_gb = st.slider(c['q_cloud'], 0, 500, 20)
    cam_hours = st.slider(c['q_cam'], 0, 10, 1)
    ai_prompts = st.slider(c['q_ai'], 0, 50, 5)

# 5. الحسابات والنتائج
if st.button(c['calc']):
    e_impact = emails * 4 * 365
    n_impact = newsletters * 0.3 * 365
    cl_impact = cloud_gb * 200 
    cam_impact = cam_hours * 150 * 365 
    ai_impact = ai_prompts * 4.5 * 365
    
    total_kg = (e_impact + n_impact + cl_impact + cam_impact + ai_impact) / 1000
    trees_needed = int(total_kg / 21)

    st.divider()
    st.header(c['res_title'])
    
    col_res, col_tree = st.columns(2)
    with col_res:
        st.metric(label=c['unit'], value=f"{total_kg:.1f} kg")
    with col_tree:
        st.metric(label="🌳 أشجار للتعويض / Trees", value=trees_needed)
    
    st.write(c['story_tree'].format(trees_needed))

    st.header(c['disc_header'])
    
    st.markdown(f"""
    <div class="discussion-card">
        <h3>🇯🇴 سياق الأردن والطاقة</h3>
        <p>{c['fact_jordan']}</p>
    </div>
    <div class="discussion-card">
        <h3>💧 الشح المائي الرقمي</h3>
        <p>{c['fact_water']}</p>
    </div>
    <div class="discussion-card">
        <h3>⚠️ التضليل الأخضر (Greenwashing)</h3>
        <p>{c['fact_green']}</p>
    </div>
    <div class="discussion-card" style="border-right-color: #FFFFFF;">
        <h3>📢 ممارسة المناصرة الرقمية</h3>
        <p>{c['advocacy_tip']}</p>
    </div>
    """, unsafe_allow_html=True)

st.caption("Eco-Digital Hub v4.1 | Discussion Mode")