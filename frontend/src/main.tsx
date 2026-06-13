import ReactDOM from "react-dom/client";

import { Provider } from "react-redux";
import { store } from "./store/store";

import { ThemeProvider } from "@mui/material/styles";
import { theme } from "./theme/theme";

import {
  QueryClientProvider,
} from "@tanstack/react-query";

import { queryClient } from "./lib/react-query";

import { GoogleOAuthProvider } from "@react-oauth/google";

import App from "./App";

// ReactDOM.createRoot(
//   document.getElementById("root")!
// ).render(
//   <Provider store={store}>
//     <ThemeProvider theme={theme}>
//       <QueryClientProvider
//         client={queryClient}
//       >
//         <App />
//       </QueryClientProvider>
//     </ThemeProvider>
//   </Provider>
// );

ReactDOM.createRoot(document.getElementById("root")!).render(
  <GoogleOAuthProvider clientId="491874201405-kom1uruvc14ctetefgh33v7pq4eb4grs.apps.googleusercontent.com">
    <Provider store={store}>
      <ThemeProvider theme={theme}>
        <QueryClientProvider client={queryClient}>
          <App />
        </QueryClientProvider>
      </ThemeProvider>
    </Provider>
  </GoogleOAuthProvider>
);