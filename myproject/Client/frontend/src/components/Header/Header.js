// Header.js
import React from 'react';
import { Layout, Menu } from 'antd';
const { Header } = Layout;

const AppHeader = () => {
  return (
    <Header style={{ position: 'fixed', zIndex: 1, width: '100%' }}>
      {/* <div className="logo"></div> */}
      <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
        <Menu.Item key="1">Home</Menu.Item>
        <Menu.Item key="2">About</Menu.Item>
        <Menu.Item key="3">Contact</Menu.Item>
      </Menu>
    </Header>
  );
};

export default AppHeader;
