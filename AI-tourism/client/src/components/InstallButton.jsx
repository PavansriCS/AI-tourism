import { Download } from "lucide-react";
import usePwaInstall from "../hooks/usePwaInstall.js";

export default function InstallButton({ className = "" }) {
  const { canInstall, install } = usePwaInstall();
  if (!canInstall) return null;
  return (
    <button onClick={install} className={`btn-secondary ${className}`}>
      <Download size={18} />
      <span>Install</span>
    </button>
  );
}

