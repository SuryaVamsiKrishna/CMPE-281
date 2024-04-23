// // import React from "react";
// // import { Button, Checkbox, Form, Input } from 'antd';

// // const onFinish = (values) => {
// //   console.log('Success:', values);
// // };
// // const onFinishFailed = (errorInfo) => {
// //   console.log('Failed:', errorInfo);
// // };

// // const Login = () => {

// //   return (
// //     <div className="flex flex-col justify-center items-center h-screen">
// //         <div className="text-[28px] font-semibold mb-6">Login</div>
// //       <Form
// //         name="basic"
// //         labelCol={{
// //           span: 8,
// //         }}
// //         wrapperCol={{
// //           span: 16,
// //         }}
// //         className="w-full max-w-md"
// //         initialValues={{
// //           remember: true,
// //         }}
// //         onFinish={onFinish}
// //         onFinishFailed={onFinishFailed}
// //         autoComplete="off"
// //       >
// //         <Form.Item
// //           label="Username"
// //           name="username"
// //           rules={[
// //             {
// //               required: true,
// //               message: "Please input your username!",
// //             },
// //           ]}
// //         >
// //           <Input />
// //         </Form.Item>

// //         <Form.Item
// //           label="Password"
// //           name="password"
// //           rules={[
// //             {
// //               required: true,
// //               message: "Please input your password!",
// //             },
// //           ]}
// //         >
// //           <Input.Password />
// //         </Form.Item>

// //         <Form.Item
// //           name="remember"
// //           valuePropName="checked"
// //           wrapperCol={{
// //             offset: 8,
// //             span: 16,
// //           }}
// //         >
// //           <Checkbox>Remember me</Checkbox>
// //         </Form.Item>

// //         <Form.Item
// //           wrapperCol={{
// //             offset: 8,
// //             span: 16,
// //           }}
// //         >
// //           <Button type="primary" htmlType="submit">
// //             Submit
// //           </Button>
// //         </Form.Item>
// //       </Form>
// //     </div>
// //   );
// // };

// // export default Login;


// import React from "react";
// import { Button, Checkbox, Form, Input } from 'antd';
// import { useNavigate } from "react-router-dom";

// const onFinish = async (values) => {
//   console.log('Received values of form:', values);

//   const requestOptions = {
//     method: 'POST',
//     headers: { 'Content-Type': 'application/json' },
//     body: JSON.stringify({
//       username: values.username,
//       password: values.password
//     })
//   };

//   try {
//     const response = await fetch('http://127.0.0.1:8000/accounts/login/', requestOptions);
//     console.log('response:', response);
//     if (!response.ok) {
//       throw new Error('Network response was not ok');
//     }
//     const data = await response.json();
//     const history = useNavigate(); 
//     console.log('Login successful:', data);
//     // Here, you can handle redirections or store the login token etc.
//     history.push('/dashboard', { username: data.username });
//   } catch (error) {
//     console.error('Failed to login:', error);
//     // Handle errors here, such as showing a notification to the user
//   }
// };

// const onFinishFailed = (errorInfo) => {
//   console.log('Failed:', errorInfo);
// };

// const Login = () => { 
//   return (
//     <div className="flex flex-col justify-center items-center h-screen">
//       <div className="text-[28px] font-semibold mb-6">Login</div>
//       <Form
//         name="basic"
//         labelCol={{ span: 8 }}
//         wrapperCol={{ span: 16 }}
//         className="w-full max-w-md"
//         initialValues={{ remember: true }}
//         onFinish={onFinish}
//         onFinishFailed={onFinishFailed}
//         autoComplete="off"
//       >
//         <Form.Item
//           label="Username"
//           name="username"
//           rules={[{ required: true, message: "Please input your username!" }]}
//         >
//           <Input />
//         </Form.Item>
//         <Form.Item
//           label="Password"
//           name="password"
//           rules={[{ required: true, message: "Please input your password!" }]}
//         >
//           <Input.Password />
//         </Form.Item>
//         <Form.Item
//           name="remember"
//           valuePropName="checked"
//           wrapperCol={{ offset: 8, span: 16 }}
//         >
//           <Checkbox>Remember me</Checkbox>
//         </Form.Item>
//         <Form.Item
//           wrapperCol={{ offset: 8, span: 16 }}
//         >
//           <Button type="primary" htmlType="submit">
//             Submit
//           </Button>
//         </Form.Item>
//       </Form>
//     </div>
//   );
// };

// export default Login;


import React from "react";
import { Button, Checkbox, Form, Input } from 'antd';
import { useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate(); // Hook moved to top level of the component

  const onFinish = async (values) => {
    console.log('Received values of form:', values);

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: values.username,
        password: values.password
      })
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/accounts/login/', requestOptions);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      console.log('Login successful:', data);
      // Navigate to Dashboard with username
      navigate('/dashboard', { state: { username: data.username } });
    } catch (error) {
      console.error('Failed to login:', error);
      // Handle errors here, such as showing a notification to the user
    }
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };

  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <div className="text-[28px] font-semibold mb-6">Login</div>
      <Form
        name="basic"
        labelCol={{ span: 8 }}
        wrapperCol={{ span: 16 }}
        className="w-full max-w-md"
        initialValues={{ remember: true }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="off"
      >
        <Form.Item
          label="Username"
          name="username"
          rules={[{ required: true, message: "Please input your username!" }]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          label="Password"
          name="password"
          rules={[{ required: true, message: "Please input your password!" }]}
        >
          <Input.Password />
        </Form.Item>
        <Form.Item
          name="remember"
          valuePropName="checked"
          wrapperCol={{ offset: 8, span: 16 }}
        >
          <Checkbox>Remember me</Checkbox>
        </Form.Item>
        <Form.Item
          wrapperCol={{ offset: 8, span: 16 }}
        >
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default Login;
