// // import { useState } from "react";
// // import { useNavigate, Link as RouterLink } from "react-router-dom";
// // import {
// //   Container,
// //   Box,
// //   Typography,
// //   TextField,
// //   Button,
// //   Divider,
// //   Alert,
// //   Link,
// //   CircularProgress,
// //   Paper,
// // } from "@mui/material";
// // import { Google as GoogleIcon } from "@mui/icons-material";
// // import { Formik, Form, Field } from "formik";
// // import * as Yup from "yup";
// // import { useGoogleLogin } from "@react-oauth/google";
// // import axios from "axios";

// // const validationSchema = Yup.object({
// //   email: Yup.string().email("Invalid email").required("Required"),
// //   password: Yup.string().min(6, "Min 6 characters").required("Required"),
// // });

// // export default function LoginPage() {
// //   const navigate = useNavigate();
// //   const [error, setError] = useState("");

// //   const handleSubmit = async (values: { email: string; password: string }) => {
// //     try {
// //       const res = await axios.post("/auth/login", values);
// //       localStorage.setItem("token", res.data.access_token);
// //       navigate("/dashboard");
// //     } catch (err: any) {
// //       setError(err.response?.data?.detail || "Login failed");
// //     }
// //   };

// //   const googleLogin = useGoogleLogin({
// //     onSuccess: async (tokenResponse) => {
// //       try {
// //         const res = await axios.post("/auth/google", {
// //           access_token: tokenResponse.access_token,
// //         });
// //         localStorage.setItem("token", res.data.access_token);
// //         navigate("/dashboard");
// //       } catch {
// //         setError("Google login failed");
// //       }
// //     },
// //     onError: () => setError("Google login failed"),
// //   });

// //   return (
// //     <Container maxWidth="sm">
// //       <Paper elevation={3} sx={{ p: 4, mt: 8 }}>
// //         <Typography variant="h4" align="center" gutterBottom>
// //           Sign In
// //         </Typography>

// //         {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}

// //         <Formik
// //           initialValues={{ email: "", password: "" }}
// //           validationSchema={validationSchema}
// //           onSubmit={handleSubmit}
// //         >
// //           {({ isSubmitting }) => (
// //             <Form>
// //               <Field
// //                 as={TextField}
// //                 fullWidth
// //                 name="email"
// //                 label="Email"
// //                 margin="normal"
// //                 autoComplete="email"
// //               />
// //               <Field
// //                 as={TextField}
// //                 fullWidth
// //                 name="password"
// //                 label="Password"
// //                 type="password"
// //                 margin="normal"
// //                 autoComplete="current-password"
// //               />
// //               <Button
// //                 type="submit"
// //                 fullWidth
// //                 variant="contained"
// //                 sx={{ mt: 2, mb: 2 }}
// //                 disabled={isSubmitting}
// //               >
// //                 {isSubmitting ? <CircularProgress size={24} /> : "Sign In"}
// //               </Button>
// //             </Form>
// //           )}
// //         </Formik>

// //         <Divider sx={{ my: 2 }}>OR</Divider>

// //         <Button
// //           fullWidth
// //           variant="outlined"
// //           startIcon={<GoogleIcon />}
// //           onClick={() => googleLogin()}
// //         >
// //           Sign in with Google
// //         </Button>

// //         <Box sx={{ mt: 2, textAlign: "center" }}>
// //           <Link component={RouterLink} to="/register" variant="body2">
// //             Don't have an account? Sign Up
// //           </Link>
// //         </Box>
// //       </Paper>
// //     </Container>
// //   );
// // }

// import { useState } from "react";
// import { useNavigate, Link as RouterLink } from "react-router-dom";
// import {
//   Container,
//   Typography,
//   TextField,
//   Button,
//   Divider,
//   Alert,
//   Link,
//   CircularProgress,
//   Paper,
//   Box,
// } from "@mui/material";

// import { GoogleLogin } from "@react-oauth/google";
// import { Formik, Form, Field } from "formik";
// import * as Yup from "yup";
// import api from "../api/axios";

// const validationSchema = Yup.object({
//   email: Yup.string().email("Invalid email").required("Required"),
//   password: Yup.string().min(6, "Min 6 characters").required("Required"),
// });

// export default function LoginPage() {
//   const navigate = useNavigate();
//   const [error, setError] = useState("");

//   const handleSubmit = async (values: any) => {
//     try {
//       const res = await api.post("/auth/login", values);

//       localStorage.setItem("token", res.data.access_token);
//       navigate("/dashboard");
//     } catch (err: any) {
//       setError(err.response?.data?.detail || "Login failed");
//     }
//   };

//   const handleGoogle = async (credentialResponse: any) => {
//     try {
//       const res = await api.post("/auth/google", {
//         credential: credentialResponse.credential,
//       });

//       localStorage.setItem("token", res.data.access_token);
//       navigate("/dashboard");
//     } catch (err) {
//       console.log(err);
//       setError("Google login failed");
//     }
//   };

//   return (
//     <Container maxWidth="sm">
//       <Paper elevation={3} sx={{ p: 4, mt: 8 }}>
//         <Typography variant="h4" align="center">
//           Sign In
//         </Typography>

//         {error && (
//           <Alert severity="error" sx={{ mb: 2 }}>
//             {error}
//           </Alert>
//         )}

//         <Formik
//           initialValues={{ email: "", password: "" }}
//           validationSchema={validationSchema}
//           onSubmit={handleSubmit}
//         >
//           {({ isSubmitting }) => (
//             <Form>
//               <Field
//                 as={TextField}
//                 fullWidth
//                 name="email"
//                 label="Email"
//                 margin="normal"
//               />

//               <Field
//                 as={TextField}
//                 fullWidth
//                 name="password"
//                 label="Password"
//                 type="password"
//                 margin="normal"
//               />

//               <Button
//                 type="submit"
//                 fullWidth
//                 variant="contained"
//                 sx={{ mt: 2 }}
//                 disabled={isSubmitting}
//               >
//                 {isSubmitting ? (
//                   <CircularProgress size={24} />
//                 ) : (
//                   "Sign In"
//                 )}
//               </Button>
//             </Form>
//           )}
//         </Formik>

//         <Divider sx={{ my: 2 }}>OR</Divider>

//         {/* GOOGLE LOGIN FIX */}
//         <Box display="flex" justifyContent="center">
//           <GoogleLogin
//             onSuccess={handleGoogle}
//             onError={() => setError("Google login failed")}
//           />
//         </Box>

//         <Box sx={{ mt: 2, textAlign: "center" }}>
//           <Link component={RouterLink} to="/register">
//             Don't have an account? Sign Up
//           </Link>
//         </Box>
//       </Paper>
//     </Container>
//   );
// }

import { useState } from "react";
import { useNavigate, Link as RouterLink } from "react-router-dom";
import {
  Container,
  Typography,
  TextField,
  Button,
  Divider,
  Alert,
  Link,
  CircularProgress,
  Paper,
  Box,
} from "@mui/material";

import { GoogleLogin } from "@react-oauth/google";
import { Formik, Form, Field } from "formik";
import * as Yup from "yup";

import api from "../api/axios";

const validationSchema = Yup.object({
  email: Yup.string().email("Invalid email").required("Required"),
  password: Yup.string().min(6, "Min 6 characters").required("Required"),
});

export default function LoginPage() {
  const navigate = useNavigate();
  const [error, setError] = useState("");

  // ======================
  // EMAIL LOGIN
  // ======================
  const handleSubmit = async (values: { email: string; password: string }) => {
    try {
      const res = await api.post("/auth/login", values);

      localStorage.setItem("token", res.data.access_token);
      navigate("/dashboard");
    } catch (err: any) {
      setError(err.response?.data?.detail || "Login failed");
    }
  };

  // ======================
  // GOOGLE LOGIN (FIXED)
  // ======================
  const handleGoogleSuccess = async (credentialResponse: any) => {
    try {
      const res = await api.post("/auth/google", {
        access_token: credentialResponse.credential, // ✅ FIXED
      });

      localStorage.setItem("token", res.data.access_token);
      navigate("/dashboard");
    } catch (err) {
      console.error(err);
      setError("Google login failed");
    }
  };

  return (
    <Container maxWidth="sm">
      <Paper elevation={3} sx={{ p: 4, mt: 8 }}>
        <Typography variant="h4" align="center">
          Sign In
        </Typography>

        {error && <Alert severity="error">{error}</Alert>}

        {/* EMAIL LOGIN */}
        <Formik
          initialValues={{ email: "", password: "" }}
          validationSchema={validationSchema}
          onSubmit={handleSubmit}
        >
          {({ isSubmitting }) => (
            <Form>
              <Field as={TextField} fullWidth name="email" label="Email" margin="normal" />
              <Field as={TextField} fullWidth name="password" label="Password" type="password" margin="normal" />

              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 2, mb: 2 }}
                disabled={isSubmitting}
              >
                {isSubmitting ? <CircularProgress size={24} /> : "Sign In"}
              </Button>
            </Form>
          )}
        </Formik>

        <Divider sx={{ my: 2 }}>OR</Divider>

        {/* GOOGLE LOGIN */}
        <Box sx={{ display: "flex", justifyContent: "center" }}>
          <GoogleLogin
            onSuccess={handleGoogleSuccess}
            onError={() => setError("Google login failed")}
          />
        </Box>

        <Box sx={{ mt: 2, textAlign: "center" }}>
          <Link component={RouterLink} to="/register">
            Don't have an account? Sign Up
          </Link>
        </Box>
      </Paper>
    </Container>
  );
}