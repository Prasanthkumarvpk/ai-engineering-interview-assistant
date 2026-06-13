import api from "../api/axios";

export const API_ENDPOINTS = {
  LOGIN: "/auth/login",
  REGISTER: "/auth/register",
};

export const loginUser = (
  data: {
    email: string;
    password: string;
  }
) => {

  return api.post(
    API_ENDPOINTS.LOGIN,
    data
  );
};

export const registerUser = (
  data: any
) => {

  return api.post(
    API_ENDPOINTS.REGISTER,
    data
  );
};