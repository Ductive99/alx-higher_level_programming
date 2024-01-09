#!/usr/bin/node
// Returns how many times an item appears in a list

exports.Occurences = function (list, searchElement) {
  return list.filter(item => item === searchElement).length;
};
