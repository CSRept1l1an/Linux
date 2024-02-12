### Basic Commands:

1. **Install a Package**:
```
yum install <package_name>
```

2. **Remove a Package**:
```
yum remove <package_name>
```

3. **Update Installed Packages**:
```
yum update
```

4. **Search for a Package**:
```
yum search <keyword>
```

5. **List Installed Packages**:
```
yum list installed
```

6. **Get Information about a Package**:
```
yum info <package_name>
```

7. **Check for Available Updates**:
```
yum check-update
```

### Additional Commands:

8. **Clean YUM Cache**:
```
yum clean all
```

9. **List Available Repositories**:
```
yum repolist
```

10. **Enable a Repository**:
 ```
 yum-config-manager --enable <repository_name>
 ```

11. **Disable a Repository**:
 ```
 yum-config-manager --disable <repository_name>
 ```

12. **List Enabled Repositories**:
 ```
 yum repolist enabled
 ```

13. **List Disabled Repositories**:
 ```
 yum repolist disabled
 ```

### Advanced Commands:

14. **Install a Specific Version**:
 ```
 yum install <package_name>-<version>
 ```

15. **List Dependencies for a Package**:
 ```
 yum deplist <package_name>
 ```

16. **Reinstall a Package**:
 ```
 yum reinstall <package_name>
 ```

17. **Check if a Package is Installed**:
 ```
 yum list installed <package_name>
 ```

18. **Clean Package Metadata and Cache**:
 ```
 yum clean metadata
 ```
