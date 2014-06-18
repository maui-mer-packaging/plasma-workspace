/***************************************************************************
 *                                                                         *
 *   Copyright 2013 Sebastian Kügler <sebas@kde.org>                       *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA .        *
 ***************************************************************************/


#ifndef SYSTEMTRAYMANAGER__H
#define SYSTEMTRAYMANAGER__H

#include <kdeclarative/qmlobject.h>

#include <QAbstractItemModel>
#include <QObject>
#include <qtextcodec.h>

#include "task.h"

class QQuickItem;

namespace SystemTray {
    class Manager;
    class Task;
}

namespace SystemTray {

class HostPrivate;

class Host : public QObject
{
    Q_OBJECT

    Q_PROPERTY(QAbstractItemModel* hiddenTasks READ hiddenTasks CONSTANT)
    Q_PROPERTY(QAbstractItemModel* shownTasks READ shownTasks CONSTANT)
    Q_PROPERTY(QAbstractItemModel* allTasks READ allTasks CONSTANT)

    Q_PROPERTY(QAbstractItemModel* availablePlasmoids READ availablePlasmoids CONSTANT)
    Q_PROPERTY(QStringList plasmoidsAllowed READ plasmoidsAllowed WRITE setPlasmoidsAllowed NOTIFY plasmoidsAllowedChanged)

    Q_PROPERTY(QStringList categories READ categories NOTIFY categoriesChanged)

    Q_PROPERTY(QStringList forcedHiddenItems READ forcedHiddenItems WRITE setForcedHiddenItems NOTIFY forcedHiddenItemsChanged)
    Q_PROPERTY(QStringList forcedShownItems READ forcedShownItems WRITE setForcedShownItems NOTIFY forcedShownItemsChanged)


    Q_PROPERTY(QQuickItem* rootItem READ rootItem WRITE setRootItem NOTIFY rootItemChanged)

public:
    Host(QObject* parent = 0);
    virtual ~Host();

    /**
     * @return a list of all known Task instances
     **/
    QList<Task*> tasks() const;

    void setRootItem(QQuickItem* rootItem);
    QQuickItem* rootItem();

    QStringList plasmoidsAllowed() const;
    void setPlasmoidsAllowed(const QStringList &plasmoids);

    QStringList forcedShownItems() const;
    void setForcedShownItems(const QStringList &items);

    QStringList forcedHiddenItems() const;
    void setForcedHiddenItems(const QStringList &items);

public Q_SLOTS:
    void init();
    bool isCategoryShown(int cat) const;
    void setCategoryShown(int cat, bool shown);
    QAbstractItemModel* hiddenTasks();
    QAbstractItemModel* shownTasks();
    QAbstractItemModel* allTasks();
    QAbstractItemModel* availablePlasmoids();
    QStringList categories() const;


Q_SIGNALS:
    void categoriesChanged();
    void rootItemChanged();
    void shownCategoriesChanged();
    void plasmoidsAllowedChanged();
    void forcedShownItemsChanged();
    void forcedHiddenItemsChanged();

private Q_SLOTS:
    void addTask(SystemTray::Task *task);
    void removeTask(SystemTray::Task *task);
    void slotTaskStatusChanged();
    void taskStatusChanged(SystemTray::Task *task);

private:
    void initTasks();
    HostPrivate* d;

};

} // namespace
#endif // SYSTEMTRAYMANAGER__H