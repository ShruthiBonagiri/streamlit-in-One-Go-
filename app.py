import streamlit as st
st.title('Title--> Hello Geeks, welcome to gfg')
st.header('Header--> Hello Geeks, welcome to gfg')
st.subheader('Subhead-->Hello world')
st.text('Text-->Hello world')
st.markdown('Hi')
st.markdown('#Hi')
st.markdown('##Hi')
st.markdown('###Hi')
st.success('Data is Submitted')
st.info('Information!')
st.error('Error!')
exp=ZeroDivisionError('Division not possible with 0')
st.exception(exp)
st.help(ZeroDivisionError)
st.write("range(1,10)")
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)
st.code('x=10\n'
"for i in range(x): \n"
    ' print(i)\n')
st.checkbox('Male')
st.checkbox('Female')
if(st.checkbox('Adult')):
    st.write("You're an adult!")

st.subheader('Radio Button')
radioButton=st.radio('select: ',('Male','Female','other'))
if(radioButton=='Male'):
    st.write("You're a Male")
elif(radioButton=='Female'):
    st.write("You're a Female")
elif(radioButton=='Other'):
    st.write("You're an Other Gender")

st.subheader('Select Box')
selectBox=st.selectbox("Data Science : ",['Data Analysis','Web scrapping','Machine learning',
                       'Deep learning','Natural language programming','Computer Vision'])
st.write("You've selected: ",selectBox)

st.header('MultiSelect Box')
multiSelBox=st.multiselect("Data Science ",['Data Analysis','Web scrapping','Machine learning',
                           'Deep learning','Natural language programming','Computer Vision'])
st.write("You've selected: ",len(multiSelBox),'courses')
st.subheader("Button")
if(st.button('Click me')):
    st.write('Thanks for clicking me')
st.subheader("Slider")
vol=st.slider('select the volume: ',0,100,step=1)
st.write('volume is: ',vol)
st.subheader("Text Input")
username=st.text_input('Username: ')
password=st.text_input('Password: ',type='password')
st.subheader("Text Area")
textArea=st.text_area('Write something interesting about yourself in 500 words')
st.write(textArea)
st.subheader("Input Date")
st.date_input('Date')
st.subheader("Input Time")
st.time_input('Time')
