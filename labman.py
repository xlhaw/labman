import streamlit as st,datetime,time
import matplotlib as mpl,pandas as pd,numpy as np,seaborn as sb,matplotlib.pyplot as plt


st.sidebar.header('测试平台后台管理系统')
nav=st.sidebar.radio(options=['订单管理','测试管理','数据管理','客户管理'],index=0,label='导航')


if nav=='数据管理':

    '''
    ## 上传数据
    '''
    
    st.selectbox('选择测试项目',['XPS','TEM',"SEM"])
    st.selectbox('选择测试单号','dfd')
    uploaded_file=st.file_uploader('选择上传文件')
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        #do something in db
        st.success('上传成功!')

    remark=st.text_area('备注信息')

    st.button('确认提交')
    if len(remark)>0:
        st.write(remark)
    '''
    ## 生成报告
    可选邮件/网盘发送，短信通知客户与否



    ## 数据分析示例

    ![Yes]('assets/NMT.jpg')
    

    '''
    st.markdown('''![Yes](assets/NMT.jpg)''')
    st.image('assets/NMT.jpg')



if nav=='订单管理':


    '''

    ## 订单示例

    '''

    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    #df=pd.read_csv(r'assets/order.csv')
    df=pd.read_excel(r'assets/order.xlsx')
    df
    #st.map(map_data)

    '''

    ## 订单确认/管理
    确认样品测试要求，拍照上传快递包裹图片，样品图片，分配测试工程师
    '''    
    col1, col2, col3 = st.beta_columns(3)
    col1.subheader('待确认')
    col1.button('20201212001SEM')
    col2.subheader('测试中')
    col2.button('20201212002BET')
    col2.button('20201212003BET')

    col3.subheader('待反馈')
    col3.button('20201212001XPS')

    

    '''

    ## 订单查询
    历史订单查询
    '''    
    option = st.selectbox(
    '订单状态',['已完成','进行中','待确认','待反馈'])

    #df=pd.read_sql('select * from order where status=""')

    st.date_input(label='查询日期',value=(datetime.date(2020,12,1),datetime.date(2020,12,30)))

    st.balloons()



    
#Your script writes to your Streamlit app from within a cached function. This code will only be called when we detect a cache "miss"
@st.cache(allow_output_mutation=True, show_spinner=True)
def generate_data():
    chart_data = pd.DataFrame(abs(np.random.randn(20, 3)*50+100),columns=['SEM', 'XPS', 'BET'])
    date=pd.date_range('2020-12-01',periods=20,freq='D')
    chart_data.index=date
    return chart_data

     

if nav=='测试管理':
    st.header('测试统计')
    st.subheader('新增测试')
    st.line_chart(generate_data())
    st.subheader('未完成测试')
    st.line_chart(generate_data())

    '''
    不同类别测试饼图，甘特图。测试时间统计
    '''
    @st.cache # Added this
    def expensive_computation(a, b):
        time.sleep(2) # This makes the function take 2s to run
        return a*b
    a = 2
    b = 21
    res = expensive_computation(a, b)
    st.write("Result:", res)
