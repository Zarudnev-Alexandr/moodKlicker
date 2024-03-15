import { useState } from "react";

export function useInterface() {

  let [currentPage, setCurrentPage] = useState('main')

  return {
    currentPage,
    setCurrentPage
  }
}