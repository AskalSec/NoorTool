#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import urllib.parse
import webbrowser
import os
import sys

def clear_screen():
    """Clear the screen based on operating system"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the program banner"""
    banner = """
      #   _   _                  _____           _ 
#   | \ | |                |_   _|         | |
#   |  \| | ___  _   _ _ __  | | ___   ___ | |
#   | . ` |/ _ \| | | | '__| | |/ _ \ / _ \| |
#   | |\  | (_) | |_| | |    | | (_) | (_) | |
#   |_| \_|\___/ \__,_|_|    \_/\___/ \___/|_|
#                                             
#        Created by: ASKAL NOUREDDIN
#        Version: 1.0 ===========================
    """
    print(banner)
    print("    NourTool - Advanced Google Search - v1.0")
    print("    Developed by: ASKAL | GitHub.com\n")

def format_search_query(query, file_type=None, site=None, intitle=None, inurl=None, date_range=None):
    """Format search query with advanced search parameters"""
    formatted_query = query
    
    if file_type:
        formatted_query += f" filetype:{file_type}"
    
    if site:
        formatted_query += f" site:{site}"
    
    if intitle:
        formatted_query += f" intitle:{intitle}"
    
    if inurl:
        formatted_query += f" inurl:{inurl}"
    
    if date_range:
        formatted_query += f" daterange:{date_range}"
    
    return formatted_query

def search_google(query):
    """Perform Google search"""
    base_url = "https://www.google.com/search?q="
    search_url = base_url + urllib.parse.quote(query)
    return search_url

def handle_file_type_search(query):
    """Search by file type"""
    file_types = {
        "1": "pdf",
        "2": "doc",
        "3": "docx",
        "4": "ppt",
        "5": "pptx",
        "6": "xls",
        "7": "xlsx",
        "8": "txt",
        "9": "rtf"
    }
    
    print("\nSelect file type to search for:")
    for key, value in file_types.items():
        print(f"{key}. {value}")
    
    choice = input("\nEnter file type number (leave empty to skip): ")
    
    if choice in file_types:
        return format_search_query(query, file_type=file_types[choice])
    
    return query

def main():
    """Main function of the program"""
    parser = argparse.ArgumentParser(description='NourTool - Advanced Google Search from command line.')
    parser.add_argument('query', nargs='?', help='Search query')
    parser.add_argument('-f', '--filetype', help='File type (e.g. pdf, doc, ppt)')
    parser.add_argument('-s', '--site', help='Search within specific site')
    parser.add_argument('-t', '--intitle', help='Search in page title')
    parser.add_argument('-u', '--inurl', help='Search in URL')
    parser.add_argument('-i', '--interactive', action='store_true', help='Interactive mode')
    
    args = parser.parse_args()
    
    # Check for interactive mode
    if args.interactive or not args.query:
        clear_screen()
        print_banner()
        
        query = input("Enter search term: ") if not args.query else args.query
        
        # Main menu
        while True:
            print("\nSelect search type:")
            print("1. Regular search")
            print("2. Search by file type")
            print("3. Search in specific site")
            print("4. Search in page title")
            print("5. Search in URL")
            print("6. Advanced search (custom)")
            print("0. Exit")
            
            choice = input("\nYour choice: ")
            
            if choice == "0":
                print("Thank you for using NourTool by ASKAL!")
                sys.exit(0)
            
            elif choice == "1":
                final_query = query
            
            elif choice == "2":
                final_query = handle_file_type_search(query)
            
            elif choice == "3":
                site = input("Enter site name (e.g. wikipedia.org): ")
                final_query = format_search_query(query, site=site)
            
            elif choice == "4":
                intitle = input("Enter words to search for in title: ")
                final_query = format_search_query(query, intitle=intitle)
            
            elif choice == "5":
                inurl = input("Enter words to search for in URL: ")
                final_query = format_search_query(query, inurl=inurl)
            
            elif choice == "6":
                print("\nCustomize advanced search:")
                file_type = input("File type (e.g. pdf) [leave empty to skip]: ")
                site = input("Site name (e.g. wikipedia.org) [leave empty to skip]: ")
                intitle = input("Search in title [leave empty to skip]: ")
                inurl = input("Search in URL [leave empty to skip]: ")
                
                final_query = format_search_query(
                    query,
                    file_type=file_type if file_type else None,
                    site=site if site else None,
                    intitle=intitle if intitle else None,
                    inurl=inurl if inurl else None
                )
            
            else:
                print("Invalid option, try again.")
                continue
            
            # Create search link
            search_url = search_google(final_query)
            
            print(f"\nFinal search query: {final_query}")
            print(f"Search URL: {search_url}")
            
            open_browser = input("\nDo you want to open the link in browser? (y/n) [y]: ").lower()
            if open_browser != "n":
                try:
                    webbrowser.open(search_url)
                    print("Browser opened!")
                except Exception as e:
                    print(f"Error opening browser: {e}")
                    print(f"You can manually copy the link: {search_url}")
            
            continue_search = input("\nDo you want to perform another search? (y/n) [y]: ").lower()
            if continue_search == "n":
                print("Thank you for using NourTool by ASKAL!")
                break
            
            new_search = input("\nDo you want to change the search term? (y/n) [n]: ").lower()
            if new_search == "y":
                query = input("Enter new search term: ")
            
            clear_screen()
            print_banner()
    
    else:
        # Execute search directly using parameters
        final_query = format_search_query(
            args.query,
            file_type=args.filetype,
            site=args.site,
            intitle=args.intitle,
            inurl=args.inurl
        )
        
        search_url = search_google(final_query)
        print(f"Search query: {final_query}")
        print(f"Search URL: {search_url}")
        
        # Open browser by default
        try:
            webbrowser.open(search_url)
        except Exception as e:
            print(f"Error opening browser: {e}")
            print(f"You can manually copy the link: {search_url}")

if __name__ == "__main__":
    main()