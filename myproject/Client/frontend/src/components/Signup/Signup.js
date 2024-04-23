// import React, { useState } from "react";
// import { Button, Checkbox, Form, Input, Select } from 'antd';

// const { Option } = Select;

// const onFinish = (values) => {
//   console.log('Success:', values);
// };
// const onFinishFailed = (errorInfo) => {
//   console.log('Failed:', errorInfo);
// };

// const Signup = () => {
//   const [userType, setUserType] = useState('staff');

//   return (
//     <div className="flex flex-col justify-center items-center h-screen">
//       <div className="text-[28px] font-semibold mb-6">Signup</div>
//       <Form
//         name="signup"
//         labelCol={{
//           span: 8,
//         }}
//         wrapperCol={{
//           span: 16,
//         }}
//         className="w-full max-w-md"
//         onFinish={onFinish}
//         onFinishFailed={onFinishFailed}
//         autoComplete="off"
//       >
//         <Form.Item
//           label="Username"
//           name="username"
//           rules={[
//             {
//               required: true,
//               message: "Please input your username!",
//             },
//           ]}
//         >
//           <Input />
//         </Form.Item>

//         <Form.Item
//           label="Email"
//           name="email"
//           rules={[
//             {
//               required: true,
//               message: "Please input your email!",
//               type: "email",
//             },
//           ]}
//         >
//           <Input />
//         </Form.Item>

//         <Form.Item
//           label="User Type"
//           name="user_type"
//           rules={[{ required: true, message: "Please select your user type!" }]}
//         >
//           <Select onChange={value => setUserType(value)}>
//             <Option value="staff">Staff</Option>
//             <Option value="driver">Driver</Option>
//           </Select>
//         </Form.Item>

//         <Form.Item
//           label="Password"
//           name="password"
//           rules={[
//             {
//               required: true,
//               message: "Please input your password!",
//             },
//           ]}
//         >
//           <Input.Password />
//         </Form.Item>

//         {userType === 'driver' && (
//           <>
//             <Form.Item
//               label="License Number"
//               name="license_number"
//               rules={[
//                 {
//                   required: true,
//                   message: "Please input your license number!",
//                 },
//               ]}
//             >
//               <Input />
//             </Form.Item>

//             <Form.Item
//               label="Vehicle Color"
//               name="vehicle_color"
//               rules={[
//                 {
//                   required: true,
//                   message: "Please input your vehicle color!",
//                 },
//               ]}
//             >
//               <Input />
//             </Form.Item>

//             <Form.Item
//               label="Model Number"
//               name="model_number"
//               rules={[
//                 {
//                   required: true,
//                   message: "Please input your model number!",
//                 },
//               ]}
//             >
//               <Input />
//             </Form.Item>

//             <Form.Item
//               label="Sensor Info"
//               name="sensor_info"
//               rules={[
//                 {
//                   required: true,
//                   message: "Please input your sensor information!",
//                 },
//               ]}
//             >
//               <Input />
//             </Form.Item>
//           </>
//         )}

//         <Form.Item
//           wrapperCol={{
//             offset: 8,
//             span: 16,
//           }}
//         >
//           <Button type="primary" htmlType="submit">
//             Submit
//           </Button>
//         </Form.Item>
//       </Form>
//     </div>
//   );
// };

// export default Signup;


import React, { useState } from "react";
import { Button, Checkbox, Form, Input, Select } from 'antd';
import { useNavigate } from "react-router-dom";

const { Option } = Select;

const Signup = () => {
  const [userType, setUserType] = useState('staff');
  const navigate = useNavigate();  // Using useNavigate for potential redirection

  const onFinish = async (values) => {
    console.log('Received values of form:', values);

    const userDetails = {
        username: values.username,
        email: values.email,
        user_type: values.user_type,
        password: values.password
    };

    let license_number = '';
    let vehicle_color = '';
    let model_number = '';
    let sensor_info = '';
    if (values.user_type === 'driver') {
        
            license_number = values.license_number;
            vehicle_color = values.vehicle_color;
            model_number = values.model_number;
            sensor_info = values.sensor_info;
        
    }

    // Create the payload with nested user object and driver details
    const payload = {
        user: userDetails,
        license_number,
        vehicle_color,
        model_number,
        sensor_info
    };

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/accounts/signup/', requestOptions);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      console.log('Signup successful:', data);
      // Redirect to some page, maybe login page or a confirmation page
      navigate('/dashboard', { state: { username: values.username } }); // Adjust according to your need
    } catch (error) {
      console.error('Failed to signup:', error);
      // Handle errors here, such as showing a notification to the user
    }
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };

  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <div className="text-[28px] font-semibold mb-6">Signup</div>
      <Form
        name="signup"
        labelCol={{ span: 8 }}
        wrapperCol={{ span: 16 }}
        className="w-full max-w-md"
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
          label="Email"
          name="email"
          rules={[{ required: true, message: "Please input your email!", type: "email" }]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="User Type"
          name="user_type"
          rules={[{ required: true, message: "Please select your user type!" }]}
        >
          <Select onChange={value => setUserType(value)}>
            <Option value="staff">Staff</Option>
            <Option value="driver">Driver</Option>
          </Select>
        </Form.Item>

        <Form.Item
          label="Password"
          name="password"
          rules={[{ required: true, message: "Please input your password!" }]}
        >
          <Input.Password />
        </Form.Item>

        {userType === 'driver' && (
          <>
            <Form.Item
              label="License Number"
              name="license_number"
              rules={[{ required: true, message: "Please input your license number!" }]}
            >
              <Input />
            </Form.Item>

            <Form.Item
              label="Vehicle Color"
              name="vehicle_color"
              rules={[{ required: true, message: "Please input your vehicle color!" }]}
            >
              <Input />
            </Form.Item>

            <Form.Item
              label="Model Number"
              name="model_number"
              rules={[{ required: true, message: "Please input your model number!" }]}
            >
              <Input />
            </Form.Item>

            <Form.Item
              label="Sensor Info"
              name="sensor_info"
              rules={[{ required: true, message: "Please input your sensor information!" }]}
            >
              <Input />
            </Form.Item>
          </>
        )}

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

export default Signup;
