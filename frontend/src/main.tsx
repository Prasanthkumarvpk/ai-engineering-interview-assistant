import ReactDOM from "react-dom/client";

import { Provider } from "react-redux";
import { store } from "./store/store";

import { ThemeProvider } from "@mui/material/styles";
import { theme } from "./theme/theme";

import {
  QueryClientProvider,
} from "@tanstack/react-query";

import { queryClient } from "./lib/react-query";

import App from "./App";

ReactDOM.createRoot(
  document.getElementById("root")!
).render(
  <Provider store={store}>
    <ThemeProvider theme={theme}>
      <QueryClientProvider
        client={queryClient}
      >
        <App />
      </QueryClientProvider>
    </ThemeProvider>
  </Provider>
);