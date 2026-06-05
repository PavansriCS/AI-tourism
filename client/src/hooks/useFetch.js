import { useEffect, useState } from "react";
import api from "../services/api.js";

export default function useFetch(path, fallback = null) {
  const [data, setData] = useState(fallback);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let active = true;
    setLoading(true);
    api.get(path)
      .then((response) => active && setData(response.data))
      .catch((err) => active && setError(err.response?.data?.message || err.message))
      .finally(() => active && setLoading(false));
    return () => {
      active = false;
    };
  }, [path]);

  return { data, loading, error };
}

