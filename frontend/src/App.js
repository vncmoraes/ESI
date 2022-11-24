import './App.css';
import React from 'react';
import { Layout } from 'antd';
const { Header, Footer, Sider, Content } = Layout;


function App() {
  return (
    <Layout>
      <Header className="App-header">Header</Header>
      <Layout className="App-layout">
        <Sider>Sider</Sider>
        <Content>Content</Content>
      </Layout>
      <Footer className="App-footer">Footer</Footer>
    </Layout >
  );
}

export default App;